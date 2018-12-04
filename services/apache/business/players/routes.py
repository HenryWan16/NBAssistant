"""
models.py is generated by flask-sqlacodegen
pip3 install flask-sqlacodegen
flask-sqlacodegen --flask --outfile models.py mysql+pymysql://user-name:password@host:port/db-schema

Example:
flask-sqlacodegen --flask --outfile models.py mysql+pymysql://twist:twist@127.0.0.1:3307/nbassistant

reference: https://www.devmashup.com/generating-flask-sqlalchemy-models-with-flask-sqlacodegen/
"""
from flask import Blueprint
from business.config import Config
from business.models import Player
from business.models import TeamPlayer
from business.models import Team
import json
import logging


players = Blueprint('players', __name__)
configuration = Config()
configuration.log_init()
logger = logging.getLogger()


@players.route("/api/player/<string:player_id>")
def player(player_id):
    """
    :param player_id:
    :return: String:
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "player_id": player_id,
            "player_name": "James Harden",
            "team_name": "Houston Rockets",
            "team_id": "1301",
            "logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/CHI.png",
            "position": "Point Guard",
            "height": 1.96,
            "weight": 100.00,
            "gender": "Male",
            "points": 9.9,
            "picture": "https://d2cwpp38twqe55.cloudfront.net/req/201811081/images/players/thorpot01.jpg",
            "description": "",
        }
    }
    """
    id_temp = int(player_id)
    player_temp = Player.query.filter_by(id=id_temp).first()

    team_player_temp = TeamPlayer.query.filter_by(player_id=id_temp).first()
    team_temp = Team.query.filter_by(id=team_player_temp.team_id).first()
    # convert Decimal to float, and then use json.dumps(res)
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "player_id": player_id,
            "player_name": player_temp.name,
            "team_name": team_temp.name,
            "team_id": str(team_temp.id),
            "logo": team_temp.logo,
            "position": player_temp.position,
            "height": player_temp.height,
            "weight": player_temp.weight,
            "gender": "Male",
            "points": float(player_temp.points),
            "picture": player_temp.photo,
            "description": player_temp.description,
        }
    }
    return json.dumps(res)


@players.route("/api/top-players/<int:number_of_players>")
def top_players(number_of_players):
    """

    :param number_of_players:
    :return:
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
    """
    players_name_list = configuration.TOP20_PLAYERS
    players_list = []
    for i in range(0, number_of_players):
        player_name = players_name_list[i]
        logger.debug(player_name)
        player_temp = Player.query.filter_by(name=player_name).first()
        team_player_temp = TeamPlayer.query.filter_by(player_id=player_temp.id).first()
        team_temp = Team.query.filter_by(id=team_player_temp.team_id).first()
        temp_player = {
            "player_id": player_temp.id,
            "player_name": player_name,
            "team_id": team_player_temp.team_id,
            "team_name": team_temp.name,
            "picture": player_temp.photo
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
    """
    :param first_character_of_last_name:
    :return:
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
    """
    players_list = []
    character = first_character_of_last_name
    player_temps = Player.query.filter_by(first_character=character)
    for player_temp in player_temps:
        player_id_temp = player_temp.id
        try:
            team_player_temp = TeamPlayer.query.filter_by(player_id=player_id_temp).first()
            team_id_temp = team_player_temp.team_id
            team_temp = Team.query.filter_by(id=team_id_temp).first()
            player_json = {
                "player_id": player_id_temp,
                "player_name": player_temp.name,
                "team_id": team_id_temp,
                "team_name": team_temp.name,
                "picture": player_temp.photo
            }
            players_list.append(player_json)
        except Exception:
            continue
    res = {
        "meta": {
            "code": 200
        },
        "data": players_list
    }
    return json.dumps(res)