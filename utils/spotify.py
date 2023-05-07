import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .settings import Settings


class Spotify:
    def __init__(self) -> None: 

        self.used = False
        
        settings = Settings()
        self.client_id = settings.load('settings.env')['spotify_client_id']
        self.client_secret = settings.load('settings.env')['spotify_client_secret']
        self.REDIRECT_URI = "http://localhost:8080"

        scope = "user-library-read user-read-playback-state user-modify-playback-state"

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(self.client_id, self.client_secret, self.REDIRECT_URI, scope=scope))

    def play_track(self, track_uri):
        self.sp.start_playback(uris=[track_uri])

    def pause_track(self):
        self.sp.pause_playback()

    def resume_track(self):
        self.sp.start_playback()

    def skip_track(self):
        self.sp.next_track()

    def previous_track(self):
        self.sp.previous_track()

    def get_current_track(self):
        return self.sp.currently_playing()

    def search(self, query):
        return self.sp.search(query, type='track', limit=1)

    def search_and_play(self, query, limit=1):
        results = self.sp.search(q=query, limit=limit)
        track_uri = results['tracks']['items'][0]['uri']
        self.play_track(track_uri)
        song_name = results['tracks']['items'][0]['name']

        return song_name