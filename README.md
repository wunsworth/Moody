# Moody
Python Script to change colour of a smart bulb based on track features

To access spotify API you need to change these variables: 

username = 'your spotify username ( you rspotify username may not be what it displays check in account settings on spotify app)

client_id, client_secret are hidden, you can make your own spotify web client here: https://developer.spotify.com/dashboard/login 

redirct_uri should be set to local host both in moods.py and in your spotify client

When running this for the first time a browser will open request access to your spotify account information, allow the app to have these permissions


If you have a lifx lamp you should change this variables: 

lifx_token = 'your lifx authorization token'

You can generate a personal access token for lifx bin your account settings, see this guide here: https://api.developer.lifx.com/docs/authentication
