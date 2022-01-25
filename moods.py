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
username ='spotify username'
scope = 'choose a scope'

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
value_list = [track_details_dict['danceability'], 
    track_details_dict['energy'], 
    track_details_dict['speechiness'], 
    track_details_dict['acousticness'], 
    track_details_dict['instrumentalness'], 
    track_details_dict['liveness']]

# find maximum value in list, map index to track features
check_array = np.asarray(value_list)
max_value = np.argmax(check_array)

try: 
    # choose colour based on value from list 
    match max_value:
        case 0:
            colour = "red"
        case 1:
            colour = "blue"
        case 2:
            colour = "green"
        case 3:
            colour = "yellow"
        case 4:
            colour = "pink"
        case 5:
            colour = "purple"
    
except:
    print('something went wrong')

# add colour to payoad of request to smartlamp
payload = {
        "color": colour,
        "power": "on"
    }

# request to smartlamp 
response =requests.put('https://api.lifx.com/v1/lights/d073d562fa17/state',
                    data=json.dumps(payload), headers=headers)

# print response from smartlamp   
print(response.text)
