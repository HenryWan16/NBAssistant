from flask import Blueprint
from business.config import Config
from business.models import Team
from business.models import Schedule
from business.models import EveryGamePredictedResult
import json
import logging


schedules = Blueprint('schedules', __name__)
configuration = Config()
configuration.log_init()
logger = logging.getLogger()


@schedules.route("/api/schedule/<string:date>")
def schedule(date):
    """
    :param date:
    :return:
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "exist": True,
            "details": [
                {
                    "date": "2018-10-16",
                    "start_time_ET": "8:00p",
                    "home": "Houston Rockets",
                    "visitor": "New Orleans Pelicans",
                    "teamA": {
                        "team_id": "13",
                        "team_name": "Houston Rockets",
                        "location": "Houston",
                        "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
                    },
                    "teamB": {
                        "team_id": "15",
                        "team_name": "New Orleans Pelicans",
                        "location": "New Orleans",
                        "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/NOH.png"
                    },
                    "winner": "Houston Rockets"
                },
                {},
                {}
            ]
        }
    }
    return json.dumps(res)
    """
    schedules_temp = Schedule.query.filter_by(date=date)
    logger.debug("Date request: " + date)
    if schedules_temp:
        schedules_list = []
        for schedule in schedules_temp:
            teamA_temp = Team.query.filter_by(id=schedule.teamA_id).first()
            teamB_temp = Team.query.filter_by(id=schedule.teamB_id).first()
            if not schedule.teamA_score or not schedule.teamB_score:
                game_predicted_result_temp = EveryGamePredictedResult.query.filter_by(Date=date, Visitor_Team=teamA_temp.name)
                winner = teamA_temp.name if float(game_predicted_result_temp.Predicted_Visitor_Score) > float(
                    game_predicted_result_temp.Predicted_Home_Score) else teamB_temp.name
            else:
                winner = teamA_temp.name if int(schedule.teamA_score) > int(schedule.teamB_score) else teamB_temp.name
            logger.debug("teamA name: " + teamA_temp.name)
            logger.debug("teamB name: " + teamB_temp.name)
            schedule_json = {
                "date": date,
                "start_time_ET": schedule.start_time_ET,
                "home": schedule.home,
                "visitor": schedule.visitor,
                "teamA": {
                    "team_id": schedule.teamA_id,
                    "team_name": teamA_temp.name,
                    "location": teamA_temp.location,
                    "logo": teamA_temp.logo,
                    "big_logo": teamA_temp.big_logo
                },
                "teamB": {
                    "team_id": schedule.teamB_id,
                    "team_name": teamB_temp.name,
                    "location": teamB_temp.location,
                    "logo": teamB_temp.logo,
                    "big_logo": teamB_temp.big_logo
                },
                "winner": winner
            }
            schedules_list.append(schedule_json)
        res = {
            "meta": {
                "code": 200
            },
            "data": {
                "exist": True,
                "details": schedules_list
            }
        }
        return json.dumps(res)
    else:
        res = {
            "meta": {
                "code": 200
            },
            "data": {
                "exist": True,
                "details": "No match on that day."
            }
        }
        return json.dumps(res)
