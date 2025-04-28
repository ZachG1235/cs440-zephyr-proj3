# website/repository.py
from .models import db, Flight

def get_flights_by_search(origin, destination, date):
    return Flight.query.filter_by(origin=origin, destination=destination, departure_date=date).all()

def add_flight(flight_data):
    new_flight = Flight(**flight_data)
    db.session.add(new_flight)
    db.session.commit()
    return new_flight
