# Business logic on Apache

1. Provide all the restful apis to clients
2. Support different kinds of queries.
3. Support all the webpages.
4. Generate models.py with flask-sqlacodegen
5. Reference: https://www.devmashup.com/generating-flask-sqlalchemy-models-with-flask-sqlacodegen/

## Unit test
Running the server without Apache2 and Docker.
1. install python3.6.4
2. export PYTHONPATH="<path_to_apache>:$PYTHONPATH"
+ Example:
+ export PYTHONPATH="/Users/henry/Workspace/NBAssistant/services/apache:$PYTHONPATH"
3. cd NBAssistant/services/apache
4. pip3 install -r requirements.txt
5. cd ./business
6. python3 run.py
7. Open a terminal, then send http requests with curl

## Testing result
```
With the help of curl, we can get all the json responses from our server.
curl -X GET "http://127.0.0.1:5000/api/home"
curl -X GET "http://127.0.0.1:5000/api/player/318"
curl -X GET "http://127.0.0.1:5000/api/players/b"
curl -X GET "http://127.0.0.1:5000/api/top-players/10"
curl -X GET "http://127.0.0.1:5000/api/team/13"
curl -X GET "http://127.0.0.1:5000/api/top-teams/10"
curl -X GET "http://127.0.0.1:5000/api/predictions"
curl -X GET "http://127.0.0.1:5000/api/prediction/8"
curl -X GET "http://127.0.0.1:5000/api/schedule/2018-11-1"
curl -X GET "http://127.0.0.1:5000/api/schedule/2018-11-3"
curl -X GET "http://127.0.0.1:5000/api/schedule/2019-12-30"
```