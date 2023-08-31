import spotipy
import json
import asyncio
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_export.common import get_creds

async def main():
    client_id, client_secret = get_creds('.client.txt')

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

    results = sp.search(q='the death of peace of mind', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
    pass
            
asyncio.run(main())