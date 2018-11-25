from flask import Flask
import json

app = Flask(__name__)

@app.route("/api/top-players/10")
def getTopplayers():
    # TODO
    res = {
        "meta": {
            "code": 200
        },
        "data": [
            {
                "player_id": 1301,
                "player_name": "James Harden",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1302,
                "player_name": "James Hardey",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1303,
                "player_name": "James Hardex",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1304,
                "player_name": "James Harder",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1305,
                "player_name": "James Hardem",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1301,
                "player_name": "James Harden",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1305,
                "player_name": "James Hardes",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1306,
                "player_name": "James Hardnes",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1307,
                "player_name": "James Hardmu",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {
                "player_id": 1308,
                "player_name": "James Hard",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            }
        ]
    }
    return json.dumps(res)