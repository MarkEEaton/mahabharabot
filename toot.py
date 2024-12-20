import random
from mastodon import Mastodon


# Create actual API instance
mastodon = Mastodon(
    access_token = 'mahabharabot_usercred.secret',
    api_base_url = 'https://mastodon.ocert.at'
)

with open('O.txt', 'r') as infile:
    toots = infile.readlines()

random_toot = random.randrange(0, len(toots) - 1)

print(toots[random_toot])
mastodon.toot(toots[random_toot])
