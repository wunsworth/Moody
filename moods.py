import spotipy
import spotipy.util as util
import json
import requests

# lifx credentials 
token2 = "lifx token"
headers = {
    "Authorization": "Bearer %s" % token2,
}

# spotify credentials
username='spotify username'
scope = 'choose a scope'

# open link to get user access
token = util.prompt_for_user_token(username,scope,client_id='',client_secret='',redirect_uri='')

# generate auth token 
spotify = spotipy.Spotify(auth=token)

# access the current track and find its ID
current_track = spotify.current_user_playing_track()
track = current_track['item']
tId = track['id']

# use track ID to find track features and add values to a list 
track_details = spotify.audio_features(tId)
track_details_dict = track_details[0]
check_list = [track_details_dict['danceability'], 
    track_details_dict['energy'], 
    track_details_dict['speechiness'], 
    track_details_dict['acousticness'], 
    track_details_dict['instrumentalness'], 
    track_details_dict['liveness']]

# find maximum value in list, map index to track features
max = 0
for i in check_list:
    if i > max:
        max = i
value = check_list.index(max)

if value == 0:
    colour = "red"
elif value == 1:
    colour = "blue"
elif value == 2:
    colour = "green"
elif value ==3:
    colour = "yellow"
elif value == 4:
    colour = "white"
elif value == 5:
    colour ="pink"
else:
    print('something went wrong')

payload = {
        "color": colour,
        "power": "on"
    }

response =requests.put('https://api.lifx.com/v1/lights/d073d562fa17/state',
                    data=json.dumps(payload), headers=headers)
            
print(response.text)