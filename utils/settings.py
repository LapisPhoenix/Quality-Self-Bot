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

        if self.debug:
            print(f"Loaded settings from {path}")

        return {"token": token, "prefix": prefix}
    
    def save(self, path: os.PathLike, settings: dict) -> None:
        """ Saves settings to the specified path. """

        with open(path, "w") as f:
            f.write(f"TOKEN={settings['token']}\n")
            f.write(f"PREFIX={settings['prefix']}\n")

        if self.debug:
            print(f"Saved settings to {path}")