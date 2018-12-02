from flask import Blueprint
import json


teams = Blueprint('teams', __name__)


@teams.route("/api/team/<string:team_id>")
def team(team_id):
    # TODO
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "team_id": team_id,
            "team_name": "Houston Rockets",
            "logo": "tiny_url",
            "location": "Houston",
            "stadium": "Toyota Center",
            "players": [
                "1302", "1201", "1336"
            ],
            "owner": "Tilman Fertitta",
            "coach": "Mike D'Antoni",
            "manager": "XXX",
            "description": "https://en.wikipedia.org/wiki/Houston_Rockets",
            "achievement": "XXXXXXXXXX"
        }
    }
    return json.dumps(res)


@teams.route("/api/top-teams/<int:number_of_teams>")
def top_teams(number_of_teams):
    # TODO
    teams_list = []
    for i in range(0, number_of_teams):
        temp_team = {
            "team_id": "1301",
            "team_name": "Houston Rockets",
            "location": "Houston",
            "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
        }
        teams_list.append(temp_team)
    res = {
        "meta": {
            "code": 200
        },
        "data": teams_list
    }
    return json.dumps(res)