from sqlalchemy.orm import Session

import models, schemas


def get_worker_by_id(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()

def get_worker_by_name(db: Session, name: str):
    return db.query(models.Worker).filter(models.Worker.name == name).first()

def get_worker_by_phone(db: Session, phone: str):
    return db.query(models.Worker).filter(models.Worker.phone_number == phone).first()

def get_all_workers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Worker).offset(skip).limit(limit).all()

def create_worker(db: Session, worker: schemas.WorkerCreate):
    db_worker = models.Worker(name=worker.name,
                              phone_number=worker.phone_number,
                              sales_points=worker.sales_points,
                              orders=worker.orders,
                              visits=worker.visits)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(name=customer.name,
                                phone_number=customer.phone_number,
                                sales_points=customer.sales_points)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_customer_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.name == name).first()

def get_customer_by_phone(db: Session, phone: str):
    return db.query(models.Customer).filter(models.Customer.phone_number == phone).first()

def get_all_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()
