from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models, schemas
from Yoko_API import crud
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


# Routes for worker(s)
class WorkerService(crud.BaseService):
    db_model = models.Worker

def get_worker_service(db: Session = Depends(get_db)):
    """Отдает объект для работы с моделью Worker с прикрепленной к ней сессией БД"""
    yield WorkerService(db)

@app.get("/workers/", response_model=list[schemas.Worker])
def read_workers(db: Session = Depends(get_db),
                 skip: int = 0,
                 limit: int = 100):
    return WorkerService(db).get_all(skip, limit)

@app.post("/worker/", response_model=list[schemas.Worker])
def create_worker(worker: schemas.WorkerCreate,
                  db: Session = Depends(get_db)):
    return WorkerService(db).create(worker)

@app.get("/worker/{worker_id}", response_model=list[schemas.Worker])
def get_worker_by_id(worker_id: int,
                     db: Session = Depends(get_db)):
    return WorkerService(db).get_by_id(worker_id)

@app.get("/worker/name/{worker_name}", response_model=list[schemas.Worker])
def get_worker_by_id(worker_name: str,
                     db: Session = Depends(get_db)):
    return WorkerService(db).get_by_name(worker_name)

@app.get("/worker/phone_number/{ph_number}", response_model=list[schemas.Worker])
def get_worker_by_id(ph_number: str,
                     db: Session = Depends(get_db)):
    return WorkerService(db).get_by_phone(ph_number)

@app.delete("/worker/{worker_id}", response_model=list[schemas.Worker])
def delete_worker_by_id(worker_id: int,
                        db: Session = Depends(get_db)):
    return WorkerService(db).delete_by_id(worker_id)


# Routers for customer
class CustomerService(crud.BaseService):
    db_model = models.Customer

@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(db: Session = Depends(get_db),
                   skip: int = 0,
                   limit: int = 100):
    return CustomerService(db).get_all(skip, limit)

@app.post("/customer/", response_model=list[schemas.Worker])
def create_customer(customer: schemas.CustomerCreate,
                    db: Session = Depends(get_db)):
    return CustomerService(db).create(customer)

@app.get("/customer/{customer_id}", response_model=list[schemas.Customer])
def get_customer_by_id(customer_id: int,
                       db: Session = Depends(get_db)):
    return CustomerService(db).get_by_id(customer_id)

@app.get("/customer/name/{customer_name}", response_model=list[schemas.Customer])
def get_customer_by_id(customer_name: str,
                       db: Session = Depends(get_db)):
    return CustomerService(db).get_by_name(customer_name)

@app.get("/customer/phone_number/{ph_number}", response_model=list[schemas.Customer])
def get_customer_by_id(ph_number: str,
                       db: Session = Depends(get_db)):
    return CustomerService(db).get_by_phone(ph_number)

@app.delete("/customer/{customer_id}", response_model=list[schemas.Customer])
def delete_customer_by_id(customer_id: int,
                          db: Session = Depends(get_db)):
    return CustomerService(db).delete_by_id(customer_id)