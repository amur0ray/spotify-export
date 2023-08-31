# shows album info for a URN or URL

from pprint import pprint
from common import get_client

urn = 'spotify:album:3p7m1Pmg6n3BlpL9Py7IUA'

sp = get_client()
album = sp.album(urn)
pprint(album)
