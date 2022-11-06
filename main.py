from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import models, schemas
import crud
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


@app.get("/workers/", response_model=List[schemas.Worker])
def read_workers(db: Session = Depends(get_db),
                 skip: int = 0,
                 limit: int = 100):
    return WorkerService(db).get_all(skip, limit)

@app.post("/worker/", response_model=schemas.WorkerCreate)
def create_worker(worker: schemas.WorkerCreate,
                  db: Session = Depends(get_db)):
    return WorkerService(db).create("worker", worker)

@app.get("/worker/{worker_id}", response_model=schemas.Worker)
def get_worker_by_id(worker_id: int,
                     db: Session = Depends(get_db)):
    return WorkerService(db).get_by_id(worker_id)

@app.get("/worker/name/{worker_name}", response_model=schemas.Worker)
def get_worker_by_name(worker_name: str,
                       db: Session = Depends(get_db)):
    return WorkerService(db).get_by_name(worker_name)

@app.get("/worker/phone_number/{ph_number}", response_model=schemas.Worker)
def get_worker_by_phone(ph_number: str,
                        db: Session = Depends(get_db)):
    return WorkerService(db).get_by_phone(ph_number)

@app.delete("/worker/{worker_id}", response_model=schemas.WorkerDelete)
def delete_worker_by_id(worker_id: int,
                        db: Session = Depends(get_db)):
    return WorkerService(db).delete_by_id(worker_id)

@app.put("/worker/{old_ph_number}", response_model=schemas.Customer)
def update_worker_phone_number(old_ph_number: str,
                               new_ph_number: str,
                               db: Session = Depends(get_db)):
    return CustomerService(db).update_phone(old_ph_number, new_ph_number)


# Routers for customer
class CustomerService(crud.BaseService):
    db_model = models.Customer

@app.get("/customers/", response_model=List[schemas.Customer])
def get_customers(db: Session = Depends(get_db),
                   skip: int = 0,
                   limit: int = 100):
    return CustomerService(db).get_all(skip, limit)

@app.post("/customer/", response_model=schemas.CustomerCreate)
def create_customer(customer: schemas.CustomerCreate,
                    db: Session = Depends(get_db)):
    return CustomerService(db).create("customer", customer)

@app.get("/customer/{customer_id}", response_model=schemas.Customer)
def get_customer_by_id(customer_id: int,
                       db: Session = Depends(get_db)):
    return CustomerService(db).get_by_id(customer_id)

@app.get("/customer/name/{customer_name}", response_model=schemas.Customer)
def get_customer_by_name(customer_name: str,
                         db: Session = Depends(get_db)):
    return CustomerService(db).get_by_name(customer_name)

@app.get("/customer/phone_number/{ph_number}", response_model=schemas.Customer)
def get_customer_by_phone(ph_number: str,
                          db: Session = Depends(get_db)):
    return CustomerService(db).get_by_phone(ph_number)

@app.delete("/customer/{customer_id}", response_model=schemas.CustomerDelete)
def delete_customer_by_id(customer_id: int,
                          db: Session = Depends(get_db)):
    return CustomerService(db).delete_by_id(customer_id)

@app.put("/customer/{old_ph_number}", response_model=schemas.Customer)
def update_customer_phone_number(old_ph_number: str,
                                 new_ph_number: str,
                                 db: Session = Depends(get_db)):
    return CustomerService(db).update_phone(old_ph_number, new_ph_number)