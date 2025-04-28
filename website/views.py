from flask import Blueprint, request, render_template, redirect, url_for
from .services import search_flights, save_flight

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/search', methods=['GET'])
def search():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    date = request.args.get('date')

    flights = search_flights(origin, destination, date)
    return render_template('results.html', flights=flights)

@views.route('/add', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        flight_data = request.form.to_dict()
        save_flight(flight_data)
        return redirect(url_for('views.home'))

    return render_template('add_flight.html')
