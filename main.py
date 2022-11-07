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
def update_worker_phone_number(obj_id: int,
                               new_ph_number: str,
                               db: Session = Depends(get_db)):
    return CustomerService(db).update_phone(obj_id, new_ph_number)


# Routes for customer(s)
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

@app.put("/customer/{obj_id}", response_model=schemas.Customer)
def update_customer_phone_number(obj_id: int,
                                 new_ph_number: str,
                                 db: Session = Depends(get_db)):
    return CustomerService(db).update_phone(obj_id, new_ph_number)


# Routes for sales point(s)
class SalesPointService(crud.BaseService):
    db_model = models.SalesPoint

@app.get("/sales_points/", response_model=List[schemas.SalesPoint])
def get_sales_points(db: Session = Depends(get_db),
                     skip: int = 0,
                     limit: int = 100):
    return SalesPointService(db).get_all(skip, limit)

@app.post("/sales_point/", response_model=schemas.SalesPointCreate)
def create_sales_point(sales_point: schemas.SalesPointCreate,
                       db: Session = Depends(get_db)):
    return SalesPointService(db).create("sales_point", sales_point)

@app.get("/sales_point/{sales_point_id}", response_model=schemas.SalesPoint)
def get_sales_point_by_id(sales_point_id: int,
                          db: Session = Depends(get_db)):
    return SalesPointService(db).get_by_id(sales_point_id)

@app.get("/sales_point/name/{sales_point_name}", response_model=schemas.SalesPoint)
def get_sales_point_by_name(sales_point_name: str,
                            db: Session = Depends(get_db)):
    return SalesPointService(db).get_by_name(sales_point_name)

@app.delete("/sales_point/{sales_point_id}", response_model=schemas.SalesPointDelete)
def delete_sales_point_by_id(sales_point_id: int,
                             db: Session = Depends(get_db)):
    return SalesPointService(db).delete_by_id(sales_point_id)

@app.put("/sales_point/{old_name}", response_model=schemas.SalesPoint)
def update_sales_point_name(obj_id: int,
                            new_name: str,
                            db: Session = Depends(get_db)):
    return SalesPointService(db).update_name(obj_id, new_name)


# Routes for order(s)
class OrderService(crud.BaseService):
    db_model = models.Order

@app.get("/orders/", response_model=List[schemas.Order])
def get_orders(db: Session = Depends(get_db),
               skip: int = 0,
               limit: int = 100):
    return OrderService(db).get_all(skip, limit)

@app.post("/order/", response_model=schemas.OrderCreate)
def create_order(order: schemas.OrderCreate,
                 db: Session = Depends(get_db)):
    return OrderService(db).create("order", order)

@app.get("/order/{order_id}", response_model=schemas.Order)
def get_order_by_id(order_id: int,
                    db: Session = Depends(get_db)):
    return OrderService(db).get_by_id(order_id)

@app.get("/order/status/{order_status}", response_model=schemas.Order)
def get_orders_by_status(order_status: str,
                         db: Session = Depends(get_db)):
    return OrderService(db).get_all_by_status(order_status)

@app.delete("/order/{order_id}", response_model=schemas.OrderCreate)
def delete_order_by_id(order_id: int,
                       db: Session = Depends(get_db)):
    return OrderService(db).delete_by_id(order_id)

@app.put("/order/{obj_id}", response_model=schemas.Order)
def update_order_name(obj_id: int,
                      new_status: str,
                      db: Session = Depends(get_db)):
    return OrderService(db).update_status(obj_id, new_status)


