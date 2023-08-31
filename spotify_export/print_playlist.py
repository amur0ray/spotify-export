from common import get_client
import logging
from pathlib import Path
import json

def track_to_json(track):
    ret = {}
    ret['name'] = track['name']
    logging.info(name)
    ret['artists'] = [artist['name'] for artist in track['artists']]
    logging.info(artists)
    return ret

sp = get_client()
logging.basicConfig(filename=f"{Path(__file__).stem}.log", level=logging.INFO)

# https://open.spotify.com/playlist/5uzeZo6MLqYe8ad23wjRR0?si=33fcbf87debd411f&pt=020c3ddc161e538c61cc4d9c551c25e7
pl_id = 'spotify:playlist:5uzeZo6MLqYe8ad23wjRR0'
offset = 0

response = sp.playlist_items(pl_id,
                                offset=offset,
                                fields='items.track.id,total',
                                additional_types=['track'])

if len(response['items']) == 0:
    exit()

out = {}
for i, item in enumerate(response['items']):
    track_id = item['track']['id']
    logging.info(track_id)
    track = sp.track(f"spotify:track:{track_id}")
    name = track['name']
    artists = [artist['name'] for artist in track['artists']]
    track_str = track_to_json(track)
    out[i] = track_str

with open(f'input_playlist_name_here.json', "w") as f:
    f.write(json.dumps(out, indent=4))

pass