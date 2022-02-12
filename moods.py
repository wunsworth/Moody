import spotipy
import spotipy.util as util
import json
import requests
import numpy as np

# lifx credentials 
lifx_token = "lifx token"
headers = {
    "Authorization": "Bearer %s" % lifx_token,
}

# spotify credentials
username ='will_u'
scope = 'user-read-currently-playing'

# open link to get user access
token = util.prompt_for_user_token(username,scope,client_id='',client_secret='',redirect_uri='')

# generate auth token
spotify = spotipy.Spotify(auth=token)

# access the current track and find its ID
current_track = spotify.current_user_playing_track()
track = current_track['item']
track_id = track['id']

# use track ID to find track features and add values to a list 
track_details = spotify.audio_features(track_id)
track_details_dict = track_details[0]
value_list = [ track_details_dict[attribute] for attribute in ['energy', 'speechiness', 'instrumentalness']]

# convert track values into rgb values
assert len(value_list) == 3, "value list of wrong length"
r, g, b = [np.floor(256 * value) for value in value_list]
print(f"rgb:{r},{g},{b}")

# add rgb value to payload
# payload = {
  #   "power": "on",
   #  "color" : rgb
# }

# request to smartlamp 
# response = requests.put('https://api.lifx.com/v1/lights/d073d562fa17/state',
  #                   data=json.dumps(payload), headers=headers)

# print response from smartlamp   
# print(response.text)

