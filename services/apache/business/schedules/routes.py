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
            "details": [
                {
                    "date": "2018-10-16",
                    "start_time_ET": "20:00",
                    "home": "Houston Rockets",
                    "visitor": "New Orleans Pelicans",
                    "teamA": {
                        "team_id": "1301",
                        "team_name": "Houston Rockets",
                        "location": "Houston",
                        "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
                    },
                    "teamB": {
                        "team_id": "1531",
                        "team_name": "New Orleans Pelicans",
                        "location": "New Orleans",
                        "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/NOH.png"
                    }
                },
                {},
                {}
            ]
        }
    }
    return json.dumps(res)