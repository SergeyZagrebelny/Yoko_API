from typing import Optional, Union
from datetime import datetime

from pydantic import BaseModel


class WorkerBase(BaseModel):
    name: str
    phone_number: str
    sales_points: Optional[list[int]] = None
    orders: Optional[list[int]] = None
    visits: Optional[list[int]] = None


class WorkerCreate(WorkerBase):
    pass


class Worker(WorkerBase):
    id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    sales_points: Optional[list[int]] = None


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True


class SalesPointBase(BaseModel):
    name: str
    workers: Optional[list[int]] = None
    orders: Optional[list[int]] = None


class SalesPointCreate(WorkerBase):
    pass


class SalesPoint(WorkerBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    created_at: datetime = datetime.now()
    closed_at: Optional[datetime] = None
    status: str = "started"
    sales_point: int
    customer: int
    worker: int
    visit: int


class OrderCreate(WorkerBase):
    pass


class Order(WorkerBase):
    id: int

    class Config:
        orm_mode = True


class VisitBase(BaseModel):
    created_at: datetime = datetime.now()
    sales_point: int
    customer: int
    worker: int
    order: int


class VisitCreate(WorkerBase):
    pass


class Visit(WorkerBase):
    id: int

    class Config:
        orm_mode = True