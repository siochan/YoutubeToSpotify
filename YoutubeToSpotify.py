# Uses Youtube Data API, Spotify Web API, Youtube-DL Library

import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

from exceptions import ResponseException

from secrets import spotify_token, spotify_user_id

class YoutubetoSpotify:
    
    def __init__(self):
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}
    
    # get youtube account
    def get_youtube_client(self):
        # Log Into Youtube (Copied from Youtube Data API)
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        # from the Youtube DATA API
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client
    
    #get liked youtube videos
    def get_liked_videos(self):
        request = self.youtube_client_videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()
        # collect each video
        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url =  "https://www.youtube.com/watch?v={}".format(
                item["id"])
            # collect song and artist name using youtube DL
            video = youtube_dl.YoutubeDL({}).extract_info(
                youtube_url, download=False
            )
            song_name = video["track"]
            artist = video["artist"]


    # make new spotify playlist
    def create_playlist(self):
        pass
    
    # get spotify song ID
    def get_spotify_uri(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )

        response = requests.get(
            query, 
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # get only first song
        uri = songs[0]["uri"]

        return uri


    # add song to new spotify playlist
    def add_song(self):
        pass