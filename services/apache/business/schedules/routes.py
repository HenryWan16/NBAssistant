from flask import Blueprint
import json


schedules = Blueprint('schedules', __name__)


@schedules.route("/api/schedule/<string:date>")
def schedule(date):
    # TODO
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "exist": True,
            "date": date,
            "start_time_ET": "20:00",
            "visitor": "New Orleans Pelicans",
            "home": "Houston Rockets",
            "teamA": {
                "team_id": "1301",
                "team_name": "Houston Rockets",
                "location": "Houston"
            },
            "teamB": {
                "team_id": "1531",
                "team_name": "New Orleans Pelicans",
                "location": "New Orleans"
            }
        }
    }
    return json.dumps(res)