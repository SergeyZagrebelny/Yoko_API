"""
Template class for CRUD operations
"""

from typing import Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import Enum
from fastapi import HTTPException

import models, schemas


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
        """Name is not necessary unique"""

        obj = self.db.query(self.db_model).filter(self.db_model.name == obj_name).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with name {obj_name} not found")
        return obj

    def get_by_phone(self, obj_ph_number: str):
        obj = self.db.query(self.db_model).filter(self.db_model.phone_number == obj_ph_number).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with phone number {obj_ph_number} not found")
        return obj

    def get_all_by_status(self, status: Enum("started", "ended", "in process", "awaiting", "canceled")):
        return self.db.query(self.db_model).filter(self.db_model.status == status).all()

    def create(self,
               entity: str,
               data: Optional[Union[schemas.WorkerCreate,
                                    schemas.CustomerCreate,
                                    schemas.SalesPointCreate,
                                    schemas.VisitCreate,
                                    schemas.OrderCreate]]):
        if entity == "worker":
            db_obj = models.Worker(name=data.name,
                                   phone_number=data.phone_number)
        elif entity == "customer":
            db_obj = models.Customer(name=data.name,
                                     phone_number=data.phone_number)
        elif entity == "sales_point":
            db_obj = models.SalesPoint(name=data.name)
        elif entity == "order":
            db_obj = models.Order(status=data.status,
                                  sales_point=data.sales_point,
                                  customer=data.sales_point,
                                  worker=data.worker,
                                  visit=data.visit)
        #elif entity == "visit":
        #    db_obj = models.Visit(name=data.name)
        else:
            raise HTTPException(status_code=400, detail=f"Person must be either worker or customer.")
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
        return f"Object with id = {obj_id} has just been deleted.", 200

    def delete_by_phone(self, obj_ph_number: str):
        obj = self.db.query(self.db_model).filter(self.db_model.ph_number == obj_ph_number).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with phone_number {obj_ph_number} not found")
        self.db.delete(obj)
        self.db.commit()
        #self.db.refresh(obj)
        return f"Object with phone number = {obj_ph_number} has just been deleted.", 200

    def update_phone(self, obj_id: int, new_ph_number: str):
        user_with_new_p_number = self.db.query(self.db_model).filter(self.db_model.phone_number == new_ph_number).first()
        if user_with_new_p_number:
            raise HTTPException(status_code=400, detail=f"Phone_number {new_ph_number} is already used.")
        obj = self.db.query(self.db_model).filter(self.db_model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with id {obj_id} not found.")
        obj.phone_number = new_ph_number
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update_name(self, obj_id: int, new_name: str):
        obj = self.db.query(self.db_model).filter(self.db_model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with id {obj_id} not found.")
        obj.name = new_name
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update_status(self, obj_id: int, new_status: Enum("started", "ended", "in process", "awaiting", "canceled")):
        obj = self.db.query(self.db_model).filter(self.db_model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with id {obj_id} not found.")
        obj.status = new_status
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj