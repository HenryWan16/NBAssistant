# NBAssistant

+ Created by: Twister team
+ Fantasy Twister (NBA Assistant)

## How to run?
1. install python3.6.4
2. download docker desktop from:
 https://www.docker.com/products/docker-desktop
3. cd NBAssistant/services/
4. docker build -t nbassistant_apache apache/
5. docker-compose up -d
6. download Sequel pro from:
 https://www.sequelpro.com/
7. login database
8. open a new terminal, and cd /NBAssistant/services
9. docker-compose down