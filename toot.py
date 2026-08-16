import os
import random
from mastodon import Mastodon

def tooter():
    # Check if O.txt exists
    if not os.path.exists('O.txt'):
        print("Error: O.txt file not found")
        return
    
    base_url = 'https://mastodon.ocert.at'
    
    # Validate that the environment variable is set
    if 'MAHABOTSECRET' not in os.environ:
        print("Error: MAHABOTSECRET environment variable not set")
        return
    
    try:
        mastodon = Mastodon(access_token=os.environ['MAHABOTSECRET'], api_base_url=base_url)

        with open('O.txt', 'r') as infile:
            toots = [line.strip() for line in infile if line.strip()]

        # Check if we have any toots
        if not toots:
            print("No toots found in O.txt")
            return

        def randomize():
            random_toot = random.randrange(0, len(toots))
            toot = toots[random_toot]
            return toot

        toot = randomize()
        
        # Validate toot length
        if len(toot) < 500:
            print(f"Posting: {toot}")
            mastodon.toot(toot)
        else:
            print("Toot too long, trying again...")
            tooter()
            
    except Exception as e:
        print(f"Error posting to Mastodon: {e}")

if __name__ == '__main__':
    tooter()
