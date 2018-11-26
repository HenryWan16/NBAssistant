from flask import Flask
from NBAssistant.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from NBAssistant.main.routes import main
    from NBAssistant.players.routes import players
    from NBAssistant.teams.routes import teams
    from NBAssistant.predictions.routes import predictions
    from NBAssistant.schedules.routes import schedules
    app.register_blueprint(main)
    app.register_blueprint(players)
    app.register_blueprint(teams)
    app.register_blueprint(predictions)
    app.register_blueprint(schedules)
    return app