from flask import Flask
from services.apache.business.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from main.routes import main
    from players.routes import players
    from teams.routes import teams
    from predictions.routes import predictions
    from schedules.routes import schedules
    app.register_blueprint(main)
    app.register_blueprint(players)
    app.register_blueprint(teams)
    app.register_blueprint(predictions)
    app.register_blueprint(schedules)
    return app