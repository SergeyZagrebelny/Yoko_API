from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/worker/", response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    db_worker = crud.get_worker_by_phone(db, phone=worker.phone_number)
    if db_worker:
        raise HTTPException(status_code=400, detail="Worker with this phone number already exists.")
    return crud.create_worker(db=db, worker=worker)


@app.get("/workers/", response_model=list[schemas.Worker])
def read_workers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workers = crud.get_all_workers(db, skip=skip, limit=limit)
    return workers


@app.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.get_worker_by_id(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker


@app.post("/customer/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_phone(db, phone=customer.phone_number)
    if db_customer:
        raise HTTPException(status_code=400, detail="Customer with this phone number already exists.")
    return crud.create_customer(db=db, customer=customer)


#@app.post("/users/{user_id}/items/", response_model=schemas.Customer)
#def create_item_for_user(
#    user_id: int, item: schemas.CustomerCreate, db: Session = Depends(get_db)
#):
#    return crud.create_customer(db=db, item=item, user_id=user_id)
#
#
#@app.get("/items/", response_model=list[schemas.Customer])
#def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    items = crud.get_items(db, skip=skip, limit=limit)
#    return items