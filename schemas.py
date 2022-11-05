from typing import Optional

from pydantic import BaseModel


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