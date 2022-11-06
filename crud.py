from typing import Optional

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

from Yoko_API import models, schemas


class BaseService:
    db_model = None

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(self.db_model).offset(skip).limit(limit).all()

    def get_by_id(self, obj_id: int):
        obj = self.db.query(self.db_model).filter(self.db_model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with id {obj_id} not found")
        return obj

    def get_by_name(self, obj_name: str):
        obj = self.db.query(self.db_model).filter(self.db_model.name == obj_name).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with name {obj_name} not found")
        return obj

    def get_by_phone(self, obj_phone_number: str):
        obj = self.db.query(self.db_model).filter(self.db_model.name == obj_phone_number).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with phone number {obj_phone_number} not found")
        return obj

    def create(self, person: Optional[schemas.WorkerCreate, schemas.CustomerCreate]):
        db_obj = models.Worker(name=person.name,
                               phone_number=person.phone_number)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_by_id(self, obj_id: int):
        obj = self.db.query(self.db_model).filter(self.db_model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with id {obj_id} not found")
        self.db.delete(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete_by_id(self, obj_phone_number:str):
        obj = self.db.query(self.db_model).filter(self.db_model.phone_number == obj_phone_number).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with phone_number {obj_phone_number} not found")
        self.db.delete(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
