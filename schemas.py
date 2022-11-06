from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    created_at: datetime = datetime.now()
    closed_at: Optional[datetime] = None
    status: str = "started"
    sales_point: int
    customer: int
    worker: int
    visit: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


class VisitBase(BaseModel):
    created_at: datetime = datetime.now()
    sales_point: int
    customer: int
    worker: int
    order: int


class VisitCreate(VisitBase):
    pass


class Visit(VisitBase):
    id: int

    class Config:
        orm_mode = True


class WorkerBase(BaseModel):
    name: str
    phone_number: str


class WorkerCreate(WorkerBase):
    pass


class Worker(WorkerBase):
    id: int
    sales_point: int = None
    orders: list[Order] = []
    visits: list[Visit] = []

    class Config:
        orm_mode = True


class SalesPointBase(BaseModel):
    name: str


class SalesPointCreate(SalesPointBase):
    pass


class SalesPoint(SalesPointBase):
    id: int
    workers: list[Worker] = []
    orders: list[Order] = []

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    name: str
    phone_number: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int
    sales_points: list[SalesPoint] = []

    class Config:
        orm_mode = True