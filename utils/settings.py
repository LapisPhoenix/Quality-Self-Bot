import os
import dotenv


class Settings:
    def __init__(self, debug: bool = False) -> None:
        self.debug = debug
    

    def load(self, path: os.PathLike) -> dict:
        """ Loads settings from the specified path. """
            
        dotenv.load_dotenv(path)
        token = os.getenv("TOKEN")
        prefix = os.getenv("PREFIX")
        channels_to_monitor = os.getenv("CHANNELS_TO_MONITOR_IDS")
        spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

        if channels_to_monitor is None:
            channels_to_monitor = ""
        if self.debug:
            print(f"Loaded settings from {path}")

        return {"token": token, "prefix": prefix, 'channels_to_monitor': channels_to_monitor,  'spotify_client_id': spotify_client_id, 'spotify_client_secret': spotify_client_secret}

    
    def save(self, path: os.PathLike, settings: dict) -> None:
        """ Saves settings to the specified path. """

        with open(path, "w", encoding='utf-8') as f:
            f.write(f"TOKEN={settings['token']}\n")
            f.write(f"PREFIX={settings['prefix']}\n")
            f.write(f"CHANNELS_TO_MONITOR_IDS={settings['channels_to_monitor']}\n")
            f.write(f"SPOTIFY_CLIENT_ID={settings['spotify_client_id']}\n")
            f.write(f"SPOTIFY_CLIENT_SECRET={settings['spotify_client_secret']}\n")

        if self.debug:
            print(f"Saved settings to {path}")