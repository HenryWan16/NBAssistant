# NBAssistant

+ Created by: Twister team
+ Fantasy Twister (NBA Assistant)

## How to run?
1. install python3.6.4
2. cd /NBAssistant/server
3. pip3 install -r requirements.txt
4. cd /NBAssistant/
5. python3 ./server/services/main.py
7. Open a terminal, then send http request with curl

```
curl -X GET "http://127.0.0.1:5000/api/top-players/10"
```