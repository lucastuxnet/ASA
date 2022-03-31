from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Numeric, SmallInteger
from flask_login import UserMixin

Base = declarative_base()

class Airports(Base):
    __tablename__ = 'airports'
    airport_id = Column(Integer, primary_key=True)
    airport_name = Column(String(64), unique=True)
    airport_city = Column(String(64))


class Flights(Base):
    __tablename__ = 'flights'
    flight_id = Column(Integer, primary_key=True)
    origin_airport = Column(String(64), ForeignKey("airports.airport_name"), nullable=False)
    dest_airport = Column(String(64), ForeignKey("airports.airport_name"), nullable=False)
    flight_date = Column(DateTime, nullable=False)
    price = Column(Numeric(6,2), nullable=False)
    capacity = Column(SmallInteger, nullable=False)
    passengers = Column(SmallInteger, nullable=False)


class Logins(UserMixin, Base):
    __tablename__ = 'passengers_logins'
    id = Column(Integer, primary_key=True)
    passenger_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(64), nullable=False)


class Reservations(Base):
    __tablename__ = 'reservations'
    reservation_id = Column(Integer, primary_key=True)
    e_ticket = Column(String(32), nullable=False, unique=True)
    passenger_id = Column(Integer, ForeignKey("passengers_logins.id"), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.flight_id"), nullable=False)
