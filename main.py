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


@app.post("/workers/", response_model=schemas.Worker)
def create_user(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    db_worker = crud.get_worker_by_name(db, name=worker.name)  # it is not necessary unique
    if db_worker:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_worker(db=db, worker=worker)


@app.get("/workers/", response_model=list[schemas.Worker])
def read_workers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workers = crud.get_workers(db, skip=skip, limit=limit)
    return workers


@app.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_user(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.get_worker(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_worker


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