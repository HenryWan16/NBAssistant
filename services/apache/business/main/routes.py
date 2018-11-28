from flask import Blueprint
import json


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/api/home")
def home():
    # TODO
    res = {
        "meta": {
            "code": 200
        },
        "data": {
            "top_players": [
                {
                    "player_id": "1301",
                    "player_name": "James Harden",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1302",
                    "player_name": "James Hardey",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1303",
                    "player_name": "James Hardex",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1304",
                    "player_name": "James Harder",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1305",
                    "player_name": "James Hardem",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1301",
                    "player_name": "James Harden",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1305",
                    "player_name": "James Hardes",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1306",
                    "player_name": "James Hardnes",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1307",
                    "player_name": "James Hardmu",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                },
                {
                    "player_id": "1308",
                    "player_name": "James Hard",
                    "team_id": "217",
                    "team_name": "Houston Rockets",
                    "picture": "tiny_url"
                }
            ],
            "top_teams": [
                {
                    "team_id": "1301",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1302",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1303",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1304",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1305",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1306",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1307",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1308",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1309",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                },
                {
                    "team_id": "1310",
                    "team_name": "Houston Rockets",
                    "location": "Houston",
                    "logo": "tiny_url"
                }
            ]
        }
    }
    return json.dumps(res)