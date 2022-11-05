from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models, schemas
from Yoko_API.CRUD import crud_customer
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

