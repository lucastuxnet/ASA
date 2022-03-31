import hashlib
from sqlalchemy import create_engine
from sqlalchemy import func
from models import Airports, Flights, Logins, Reservations
from settings import DATABASE_URL
from flask_login import login_user, logout_user
from database import SessionLocal
from datetime import datetime, timedelta

engine = create_engine(DATABASE_URL, convert_unicode=True)

########### LOGIN

def controller_load_user(user_id):
    session = SessionLocal()
    session.execute("SET search_path TO sch_tickets")
    return session.query(Logins).filter_by(id=user_id).first()

def controller_login(credentials):
    session = SessionLocal()
    session.execute("SET search_path TO sch_tickets")
    password = credentials["password"]
    hash_obj = hashlib.md5(f"{password}".encode())
    md5_value = hash_obj.hexdigest()
    user = (
        session.query(Logins)
        .filter_by(email=credentials["email"], password=credentials["password"])
        .first()
    )
    print(user)
    login_user(user)
    session.close()
    return "Logged In"

def controller_logout():
    logout_user()
    return "Logged Out"

###########################

def return_airports():
    session = SessionLocal()
    session.execute("SET search_path TO sch_tickets")
    airportsobj = session.query(Airports).all()
    session.close()
    return [
        {'Airport': airport.airport_name}
        for airport in airportsobj
        ]

def return_airport_by_origin(origin):
    session = SessionLocal()
    session.execute("SET search_path TO sch_tickets")
    airportsobj = session.query(Flights).filter_by(origin_airport=origin).all()
    session.close()
    return [
        {'Airport': airport.dest_airport}
        for airport in airportsobj
        ]

def return_flights_by_date(date):
    date2 = datetime.strptime(date, '%Y-%m-%d') + timedelta(1)
    date2 = date2.strftime('%Y-%m-%d')
    session = SessionLocal()
    session.execute("SET search_path TO sch_tickets")
    flightsobj = (
        session.query(Flights)
        .filter( (Flights.flight_date >= date) & (Flights.flight_date < date2) )
        .all()
    )
    session.close()
    return [
        {'Origin' : flight.origin_airport, 
        'Destination' : flight.dest_airport, 
        'Price': str(flight.price)}
        for flight in flightsobj
    ]


def return_flights_by_price(data):
    passengers_n = int(data["passengers"])
    session = SessionLocal()
    session.execute("SET search_path TO sch_tickets")
    flightsobj = (
        session.query(Flights).filter_by(price=(session.query(func.min(Flights.price))))
        .all()
    )
    session.close()
    return [
        {'Origin' : flight.origin_airport, 
        'Destination' : flight.dest_airport, 
        'Date' : flight.flight_date,
        'Price': str((flight.price*passengers_n))}
        for flight in flightsobj
    ]


def insert_reservations(data):
    eticket = (
        str(datetime.now().day) 
        + str(datetime.now().month) 
        + str(datetime.now().year)
        + str(datetime.now().hour)
        + str(datetime.now().minute)
        + str(datetime.now().second)
    )
    passengers_etickets = {}
    ids = list(str(data["passengersids"]).split(sep=','))
    session = SessionLocal()
    session.execute("SET search_path TO sch_tickets")
    for n, passenger in enumerate(ids):
        ticket = Reservations(
            e_ticket = eticket + f'{n}',
            passenger_id = passenger,
            flight_id = data["flightid"]
        )
        passengers_etickets[f"{passenger}"] = eticket + f'{n}'
        session.add(ticket)
    session.commit()
    session.close()

    return passengers_etickets
