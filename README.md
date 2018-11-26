# NBAssistant

+ Created by: Twister team
+ Fantasy Twister (NBA Assistant)

## How to run?
1. install python3.6.4
2. export PYTHONPATH="<parent_of_NBAssistant>:$PYTHONPATH"
+ Example: if NBAssistant is in the dir Workspace
+ export PYTHONPATH="/Users/henry/Workspace:$PYTHONPATH"
3. cd /NBAssistant/server
4. pip3 install -r requirements.txt
5. cd /NBAssistant/
6. python3 run.py
7. Open a terminal, then send http requests with curl

```
curl -X GET "http://127.0.0.1:5000/api/home"
curl -X GET "http://127.0.0.1:5000/api/top-players/10"
curl -X GET "http://127.0.0.1:5000/api/top-teams/10"
curl -X GET "http://127.0.0.1:5000/api/predictions"
curl -X GET "http://127.0.0.1:5000/api/prediction/1301"
curl -X GET "http://127.0.0.1:5000/api/schedule/2018-12-01"
```