from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from database import Base


class Worker(Base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,)
    phone_number = Column(String, unique=True, index=True)

    sales_points = relationship("SalesPoint", back_populates="workers")
    orders = relationship("Order", back_populates="performer")
    visits = relationship("Visit", back_populates="performer")

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String, unique=True, index=True)
    sales_points = Column(Integer, ForeignKey("sales_point.id"))

    orders = relationship("Order", back_populates="order")
    visits = relationship("Visit", back_populates="author")

class SalesPoint(Base):
    __tablename__ = "sales_point"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    workers = Column(Integer, ForeignKey("worker.id"))


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)
    where_to = Column(Integer, ForeignKey("sales_point.id"))
    author = Column(Integer,  ForeignKey("customer.id"))
    status = Column(Enum("started", "ended", "in process", "awaiting", "canceled", name='status_types'),
                    default="started")
    performer = Column(Integer, ForeignKey("worker.id"))

    visit = relationship("Visit", back_populates="Order", uselist=False)


class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    where_to = Column(Integer, ForeignKey("sales_point.id"))
    performer = Column(Integer, ForeignKey("worker.id"))
    author = Column(Integer, ForeignKey("customer.id"))
    order_id = Column(Integer, ForeignKey("order.id"))

    order = relationship("Order", back_populates="visit")

