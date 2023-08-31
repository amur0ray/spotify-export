import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_creds(path):
    with open(path) as f:
        js = json.loads(f.read())
        client_id, client_secret = js.values()

    return client_id, client_secret

def get_client(path='.client.json'):
    with open(path) as f:
        js = json.loads(f.read())
        client_id, client_secret = js.values()
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))