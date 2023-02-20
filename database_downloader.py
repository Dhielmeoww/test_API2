import requests
import json

r = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
f = open("cards.json", 'w')
f.write(json.dumps(json.loads(r.content.decode()), indent=4))