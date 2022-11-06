"""
Template class for CRUD operations
"""

from typing import Optional, Union

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

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
        obj = self.db.query(self.db_model).filter(self.db_model.name == obj_ph_number).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with phone number {obj_ph_number} not found")
        return obj

    def create(self, person: Optional[Union[schemas.WorkerCreate,
                                      schemas.CustomerCreate]]):
        db_obj = models.Worker(name=person.name,
                               phone_number=person.phone_number)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return f"Object {db_obj} has just been created.", 200

    def delete_by_id(self, obj_id: int):
        obj = self.db.query(self.db_model).filter(self.db_model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with id {obj_id} not found")
        self.db.delete(obj)
        self.db.commit()
        #self.db.refresh(obj)
        return f"Object with id = {obj_id} has just been deleted.", 200

    def delete_by_phone(self, obj_ph_number: str):
        obj = self.db.query(self.db_model).filter(self.db_model.ph_number == obj_ph_number).first()
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object with phone_number {obj_ph_number} not found")
        self.db.delete(obj)
        self.db.commit()
        self.db.refresh(obj)
        return f"Object with phone number = {obj_ph_number} has just been deleted.", 200

    def update_phone(self, old_ph_number: str, new_ph_number: str):
        user_with_new_p_number = self.db.query(self.db_model).filter(self.db_model.phone_number == new_ph_number).first()
        if user_with_new_p_number:
            raise HTTPException(status_code=400, detail=f"Phone_number {new_ph_number} is already in use")
        obj = self.db.query(self.db_model).filter(self.db_model.phone_number == old_ph_number).first()
        obj.phone_number = new_ph_number
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update_name(self, ph_number: str, new_name: str):
        user_with_p_number = self.db.query(self.db_model).filter(self.db_model.phone_number == ph_number).first()
        if not user_with_p_number:
            raise HTTPException(status_code=404, detail=f"Object with phone number {ph_number} not found")
        obj = self.db.query(self.db_model).filter(self.db_model.phone_number == ph_number).first()
        obj.name = new_name
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj