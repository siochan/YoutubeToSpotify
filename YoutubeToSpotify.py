# Uses Youtube Data API, Spotify Web API, Youtube-DL Library

import json
import requests
from secret import spotify_user_id, spotify_token
class YoutubetoSpotify:
    
    def __init__(self):
        self.user_id = spotify_user_id
    
    # get youtube account
    def get_youtube_client(self):
        pass
    
    #get liked youtube videos
    def get_liked_videos(self):
        pass

    # make new spotify playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name":"Youtube Liked Videos",
            "description":"All Liked Youtube Videos",
            "public":True
        })

        #endpoint
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        # playlist ID
        response_json = response.json()

        return response_json["id"]
    
    # get spotify song ID
    def get_spotify_uri(self):
        pass

    # add song to new spotify playlist
    def add_song(self):
        pass