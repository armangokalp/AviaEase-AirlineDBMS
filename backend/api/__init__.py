from flask import Blueprint

# Import blueprints from each module
from .flights import flights
from .roster import roster
from .passengers import passengers
from .cabin_crew import cabin_crew
from .pilots import pilots
from .flight_views import flight_views

def register_blueprints(app):
    app.register_blueprint(flights, url_prefix='/api')
    app.register_blueprint(roster, url_prefix='/api')
    app.register_blueprint(passengers, url_prefix='/api')
    app.register_blueprint(cabin_crew, url_prefix='/api')
    app.register_blueprint(pilots, url_prefix='/api')
    app.register_blueprint(flight_views, url_prefix='/api')