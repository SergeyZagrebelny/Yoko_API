from sqlalchemy.orm import Session

import models, schemas


def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()


def get_worker_by_name(db: Session, name: str):
    return db.query(models.Worker).filter(models.Worker.email == name).first()


def get_workers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Worker).offset(skip).limit(limit).all()


def create_worker(db: Session, worker: schemas.WorkerCreate):
    db_worker = models.Worker(name=worker.name, phone_number=worker.phone_number)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: schemas.Customer, user_id: int):
    db_customer = models.Customer(name=customer.name, phone_number=customer.phone_number)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer