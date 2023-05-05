# Uses Youtube Data API, Spotify Web API, Youtube-DL Library

class YoutubetoSpotify:
    
    def __init__(self):
        pass
    
    # get youtube account
    def get_youtube_client(self):
        pass
    
    #get liked youtube videos
    def get_liked_videos(self):
        pass

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