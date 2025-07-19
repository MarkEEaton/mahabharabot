import os
import random
from mastodon import Mastodon


base_url = 'https://mastodon.ocert.at'
mastodon = Mastodon(access_token=os.environ['MAHABOTSECRET'], api_base_url=base_url)

with open('O.txt', 'r') as infile:
    toots = infile.readlines()

def randomize():
    random_toot = random.randrange(0, len(toots) - 1)
    toot = toots[random_toot]
    return toot

def tooter():
    toot = randomize()
    if len(toot) < 500:
        print(toot)
        mastodon.toot(toot)
    else:
        tooter()

tooter()
