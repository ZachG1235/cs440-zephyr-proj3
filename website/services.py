from .repository import get_flights_by_search, add_flight

def search_flights(origin, destination, date):
    flights = get_flights_by_search(origin, destination, date)
    return flights

def save_flight(flight_data):
    return add_flight(flight_data)
