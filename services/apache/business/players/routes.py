from flask import Blueprint
import json


players = Blueprint('players', __name__)


@players.route("/api/player/<string:player_id>")
def player(player_id):
    # TODO
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "player_id": player_id,
            "player_name": "James Harden",
            "team_name": "Houston Rockets",
            "team_id": "1301",
            "position": "Point Guard",
            "height": 1.96,
            "weight": 100.00,
            "gender": "Male",
            "points": 9.9,
            "picture": "https://d2cwpp38twqe55.cloudfront.net/req/201811081/images/players/thorpot01.jpg",
            "description": "",
            "predictions": {
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
    return json.dumps(res)


@players.route("/api/top-players/<int:number_of_players>")
def top_players(number_of_players):
    # TODO
    players_list = []
    for i in range(0, number_of_players):
        temp_player = {
            "player_id": "1301",
            "player_name": "James Harden",
            "team_id": "217",
            "team_name": "Houston Rockets",
            "picture": "https://d2cwpp38twqe55.cloudfront.net/req/201811081/images/players/abrinal01.jpg"
        }
        players_list.append(temp_player)

    res = {
        "meta": {
            "code": 200
        },
        "data": players_list
    }
    return json.dumps(res)


@players.route("/api/players/<string:first_character_of_last_name>")
def player_with_specific_last_name(first_character_of_last_name):
    # TODO
    players_list = []
    for i in range(0, 35):
        temp_player = {
            "player_id": "1301",
            "player_name": "James Harden",
            "team_id": "217",
            "team_name": "Houston Rockets",
            "picture": "https://d2cwpp38twqe55.cloudfront.net/req/201811081/images/players/abrinal01.jpg"
        }
        players_list.append(temp_player)
    res = {
        "meta": {
            "code": 200
        },
        "data": players_list
    }
    return json.dumps(res)
