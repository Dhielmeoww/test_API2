import requests
import json
import time
import os
import imghdr
from requests.adapters import HTTPAdapter, Retry

if not os.path.exists('cards'):
    os.makedirs('cards')

r = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
cards = json.loads(r.content.decode())
num_cards = len(cards['data'])

i = 1
for card in cards['data']:
    print("Downloaded "+str(i)+" from "+str(num_cards)+" images", end="\r")
    if os.path.exists('cards/'+str(card['id'])+'.jpg'):
        if imghdr.what('cards/'+str(card['id'])+'.jpg') == 'jpeg':
            i += 1
            continue
    img = card['card_images'][0]['image_url_cropped']
    
    open('cards/'+str(card['id'])+'.jpg', 'wb').write(requests.get(img).content)
    time.sleep(0.3)
    i += 1

print("Done")