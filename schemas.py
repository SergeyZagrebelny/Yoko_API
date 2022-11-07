from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    created_at: datetime = datetime.now()
    status: str = "awaiting"
    sales_point: int
    customer: int
    worker: int
    visit: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    closed_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class VisitDelete(BaseModel):

    class Config:
        orm_mode = True


class VisitCreate(VisitDelete):
    created_at: datetime = datetime.now()
    sales_point: int
    customer: int
    worker: int
    order: int


class Visit(VisitCreate):
    id: int


class WorkerDelete(BaseModel):

    class Config:
        orm_mode = True


class WorkerCreate(WorkerDelete):
    name: str
    phone_number: str


class Worker(WorkerCreate):
    id: int
    sales_point: int = None
    orders: list[Order] = []
    visits: list[Visit] = []


class SalesPointDelete(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SalesPointCreate(SalesPointDelete):
    pass


class SalesPoint(SalesPointDelete):
    id: int
    workers: list[Worker] = []
    orders: list[Order] = []


class CustomerDelete(BaseModel):

    class Config:
        orm_mode = True


class CustomerCreate(CustomerDelete):
    name: str
    phone_number: str


class Customer(CustomerCreate):
    id: int
    sales_points: list[SalesPoint] = []
    orders: list[Order] = []
    visits: list[Visit] = []