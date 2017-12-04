# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 15:12:20 2017

@author: TapperR
"""

import spotipy
import pbl
from spotipy.oauth2 import SpotifyClientCredentials
import urllib
import json
import pandas as pd


#get all artists with 'rihanna' in their artist names
client_credentials_manager = SpotifyClientCredentials(client_id = '5c96a41586b5462d811dc1fc0a57dcb6', client_secret = '2f1189d85ee448a99bd1129ccfa10549')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
name = 'Rihanna'
results = sp.search(q='artist:' + name, type='artist')
print results  


data2 = json.loads(results.read())
data2 = pd.DataFrame(data2) 

#pbl.spotify_access_token()



#get information about own playlist
playlists = sp.user_playlists('spotify')  
playlists = sp.user_playlist('11127823027', playlist_id = 'spotify:user:11127823027:playlist:4q2EdEdze8KOt9DcwWzsfd') 
# sp.user_playlist('ailujadu', playlist_id)
#pbl.spotify_access_token()