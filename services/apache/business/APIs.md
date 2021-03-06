# Restful APIs
+ Pay attention that all ids are String instead of Integer

## Home Page:
### GET
/api/home
+ It will get 10 top players and 10 top teams
+ Response a JSON:

```JSON
{
    "meta": {
        "code": 200
    },
    "data": {
        "top_players": [
            {
                "player_id": 1301,
                "player_name": "James Harden",
                "team_id": 217,
                "team_name": "Houston Rockets",
                "picture": "tiny_url"
            },
            {}
        ],
        "top_teams": [
            {
                "team_id": 1301,
                "team_name": "Houston Rockets",
                "location": "Houston",
                "logo": "tiny_url"
            },
            {}
        ]
    }
}
```

### GET 
/api/top-players/<number_of_players>
```
Example1: 
GET /api/top-players/10
Get top 10 players list

Example2: 
GET /api/top-players/20
Get top 20 players list
```
+ It will return top <number_of_players> players based on the total prediction score.
+ Response a JSON 
```JSON
{
	"meta": {
		"code": 200
	},
	"data": [
		{
			"player_id": "1301",
			"player_name": "James Harden",
			"team_id": "217",
			"team_name": "Houston Rockets",
			"picture": "tiny_url"
		},
		{}
	]
}
```

### GET
/api/top-teams/<number_of_teams>
```
Example1: 
GET /api/top-teams/10
Get top 10 teams list

Example2: 
GET /api/top-teams/20
Get top 20 teams list
```

+ It will return top <number_of_teams> teams based on the total prediction score.
+ Response a JSON

```JSON
{
	"meta": {
		"code": 200
	},
	"data": [
		{
			"team_id": "1301",
			"team_name": "Houston Rockets",
			"location": "Houston",
			"logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
		},
		{}
	]
}
```

### GET
/api/players/<first_character_of_last_name>
```
Example:
GET /api/players/a
Get information about all the players whose last name is 'a'
```
Response:
```JSON
{
	"meta": {
		"code": 200
	},
	"data": [
        {
    	    "player_id": "12",
            "player_name": "James Harden",
            "team_name": "Houston Rockets",
            "team_id": "1301",
            "picture": "tiny_url"
        },
        {},
        {}
    ]
}
```

### GET
/api/player/<player_id>
```
Example:
GET /api/player/21
Get information about player 21, 21 is player_id 
```

Response:
```JSON
{
	"meta": {
		"code": 200
	},
	"data": {
	    "player_id": "12",
        "player_name": "James Harden",
        "team_name": "Houston Rockets",
        "team_id": "1301",
        "position": "Point Guard",
        "height": 1.96,
        "weight": 100.00,
        "gender": "Male",
        "points": 9.9,
        "picture": "tiny_url",
        "description": "https://en.wikipedia.org/wiki/James_Harden",
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
```

### GET
/api/team/<team_id>
```
Example:
GET /api/team/1321
Get information about team 1321, 1321 is team_id
```

Response:
```JSON
{
	"meta": {
		"code": 200
	},
	"data": {
		"team_id": "1321",
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
```

### GET
/api/schedule/<date>
```
Example:
GET /api/schedule/2018-10-16
Get schedule on that day. If there is a match on that day,
"exist" will be True, or it will be "false".
```

Response:
```JSON
{
	"meta": {
		"code": 200
	},
	"data": {
		"exist": true,
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
				},
				"winner": "Houston Rockets"
			},
			{},
			{}
		]
	}
}
```

Response (no match on that day)
```JSON
{
	"meta": {
		"code": 200
	},
	"data": {
		"exist": false,
		"date": "2018-10-16"
	}
}
```

### GET
/api/prediction/<team_id>
```
Example:
GET /api/prediction/1301
Get prediction about team 1301. If 1301 compete with others,
what the result will be.
Here "scoreA" is the predicted score for team with <teamID>.
```

Response:
```JSON
{
	"meta": {
		"code": 200
	},
	"data": [
		{
			"team_id": "1208",
			"team_name": "Houston Rockets",
			"logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png",
			"scoreA": 32,
			"scoreB": 23
		},
		{},
		{}
	]
}
```

### GET
/api/predictions
```
Return current prediction about this NBA season.
```

Response:
```JSON
{
	"meta": {
		"code": 200
	},
	"data": {
		"champion": {
			"east_champion": {
				"team_id": 1301,
				"team_name": "Houston Rockets",
				"logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
			},
			"west_champion": {
				"team_id": 1301,
				"team_name": "Houston Rockets",
				"logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
			},
			"final_champion": {
				"team_id": 1301,
				"team_name": "Houston Rockets",
				"logo": "https://d2p3bygnnzw9w3.cloudfront.net/req/201811271/tlogo/bbr/HOU.png"
			}
		},
		"teams_to_play_off": {
			"east_candidates": [
				1302, 1311, 5320, 1278, 1302, 1311, 5320, 1278
			],
			"west_candidates": [
				1302, 1311, 5320, 1278, 1302, 1311, 5320, 1278
			]
		},
		"MVP": {
			"player_id": 13,
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
```