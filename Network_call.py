import requests
import json


url = "https://www.fih.hockey/default.aspx?methodtype=3&client=8696669363&sport=5&league=0&timezone=0530&language=en&gamestate=4"

payload={}
headers = {
  'Cookie': 'ASP.NET_SessionId=lchjzkkjybmrsys5jkoh5ma1'
}
all_players = []
response = requests.request("GET", url, headers=headers, data=payload)
data=response.text
data = json.loads(data)
data = data["matches"]

for dt in data:
    dt = dt["participants"]
    for players in dt:
        all_players.extend(players['players_involved'])
        print(all_players)
        print(len(all_players))


