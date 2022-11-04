from typing import Union

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    sales_points: list[int]

class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True


class WorkerBase(BaseModel):
    name: str
    phone_number: str
    sales_points: list[int]
    orders: list[int]
    visits: list[int]


class WorkerCreate(WorkerBase):
    pass


class Worker(WorkerBase):
    id: int

    class Config:
        orm_mode = True