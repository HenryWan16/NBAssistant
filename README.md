# NBAssistant
NBA schedule come from:
https://www.basketball-reference.com

+ Created by: Twister team
+ Fantasy Twister (NBA Assistant)

## How to run?
1. install python3.6.4
2. download docker desktop from:
 https://www.docker.com/products/docker-desktop
3. cd NBAssistant/crawlers/
4. docker build -t nbassistant_web_crawler src/
5. cd NBAssistant/services/apache/business/
6. set config.py
+ make SQLALCHEMY_DATABASE_URI to your IP address.
7. cd NBAssistant/services/
8. docker build -t nbassistant_apache apache/
9. cd NBAssistant/crawlers/
10. docker-compose up -d
11. cd NBAssistant/services/
12. docker-compose up -d
11. download Sequel pro from:
 https://www.sequelpro.com/
13. login database
14. open a new terminal, and cd /NBAssistant/services
15. docker-compose down
16. open a new terminal, and cd /NBAssistant/crawlers
17. docker-compose down

## How to upload CSV to MySQL with Sequelpro?
1. docker ps 
+ Make sure all the services is running.

2. docker-compose kill crawler
+ Kill the web crawler

3. docker-compose rm crawler
+ Remove the container crawler

4. cd NBAssistant/crawlers/mysql
5. Open Sequel pro and past schema.sql into it
6. Import all the csv data to mysql

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
curl -X GET "http://127.0.0.1:5000/api/schedule/2018-11-23"
curl -X GET "http://127.0.0.1:5000/api/schedule/2019-12-30"
```