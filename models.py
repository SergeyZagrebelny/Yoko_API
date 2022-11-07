from sqlalchemy import (Column,
                        CHAR,
                        ForeignKey,
                        Integer,
                        DateTime,
                        Enum,
                        SmallInteger)
from sqlalchemy.orm import relationship

from database import Base


class Worker(Base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(CHAR(255))
    phone_number = Column(CHAR(255), unique=True, index=True)
    sales_point_id = Column(Integer,
                            ForeignKey("sales_point.id"),)

    sales_point = relationship("SalesPoint", back_populates="workers")
    orders = relationship("Order", back_populates="worker")
    visits = relationship("Visit", back_populates="worker")


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(CHAR(255))
    phone_number = Column(CHAR(255), unique=True, index=True)
    sales_point = Column(Integer,
                         ForeignKey("sales_point.id"),)

    orders = relationship("Order", back_populates="customer")
    visits = relationship("Visit", back_populates="customer")


class SalesPoint(Base):
    __tablename__ = "sales_point"

    id = Column(SmallInteger, primary_key=True, index=True)  #for memory economy reasons only
    name = Column(CHAR(255))

    workers = relationship("Worker", back_populates="sales_point")
    orders = relationship("Order", back_populates="sales_point")


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)
    status = Column(Enum("started", "ended", "in process", "awaiting", "canceled",
                         name='status_types'),
                    default="awaiting")
    sales_point_id = Column(Integer,
                            ForeignKey("sales_point.id"))
    sales_point = relationship("SalesPoint",
                               back_populates="orders",
                               foreign_keys=[sales_point_id])

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="orders", foreign_keys=[customer_id])

    worker_id = Column(Integer,
                       ForeignKey("worker.id"),)
    worker = relationship("Worker", back_populates="orders", foreign_keys=[worker_id])

    visit = relationship("Visit", back_populates="order", uselist=False)


class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    sales_point = Column(Integer,
                         ForeignKey("sales_point.id"),)
    sales_point_id = Column(Integer,
                            ForeignKey("worker.id"),)
    worker = relationship("Worker",
                          back_populates="visits",
                          foreign_keys=[sales_point_id])

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="visits", foreign_keys=[customer_id])

    order_id = Column(Integer, ForeignKey("order.id"))
    order = relationship("Order", back_populates="visit", foreign_keys=[order_id])

