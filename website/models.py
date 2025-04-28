from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Flight {self.origin} to {self.destination} on {self.departure_date}>'
