from typing import Union

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    phone_number: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
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

    class Config:
        orm_mode = True