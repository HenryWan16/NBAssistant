from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from business.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from business.main.routes import main
    from business.players.routes import players
    from business.teams.routes import teams
    from business.predictions.routes import predictions
    from business.schedules.routes import schedules
    app.register_blueprint(main)
    app.register_blueprint(players)
    app.register_blueprint(teams)
    app.register_blueprint(predictions)
    app.register_blueprint(schedules)
    return app