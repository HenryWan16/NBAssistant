from flask import Blueprint
import json


predictions = Blueprint('predictions', __name__)


@predictions.route("/api/predictions")
def getPredictions():
    # TODO
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "champion": {
                "east_champion": {
                    "team_id": "1301",
                    "team_name": "Houston Rockets",
                    "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
                },
                "west_champion": {
                    "team_id": "1301",
                    "team_name": "Houston Rockets",
                    "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
                },
                "final_champion": {
                    "team_id": "1301",
                    "team_name": "Houston Rockets",
                    "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
                }
            },
            "teams_to_play_off": {
                "east_candidates": [
                    "1302", "1311", "5320", "1278", "1302", "1311", "5320", "1278"
                ],
                "west_candidates": [
                    "1302", "1311", "5320", "1278", "1302", "1311", "5320", "1278"
                ]
            },
            "MVP": {
                "player_id": "13",
                "player_name": "James Harden",
                "picture": "https://d2cwpp38twqe55.cloudfront.net/req/201811081/images/players/abrinal01.jpg",
                "prediction": {
                    "statistics": {
                        "points": 9.9,
                        "rebounds": 3.2,
                        "assists": 1.8,
                        "blocks": 0.3,
                        "steals": 1.1,
                        "turnovers": 1.4
                    }
                }
            }
        }
    }
    return json.dumps(res)


@predictions.route("/api/prediction/<string:team_id>")
def team_prediction(team_id):
    # TODO
    res = {
        "meta": {
            "code": 200
        },
        "data": [
            {
                "team_id": team_id,
                "team_name": "Houston Rockets",
                "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png",
                "scoreA": 32,
                "scoreB": 23
            },
            {},
            {}
        ]
    }
    return json.dumps(res)