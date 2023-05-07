import json
import requests
from concurrent.futures import ThreadPoolExecutor

""" An asynchronous request wrapper. """


class Request:
    def __init__(self, debug: bool = False) -> None:
        self.debug = debug


    def fetch(self, url: str) -> dict:
        """ Fetches content from the specified URL. """
        response = requests.get(url)
        content = response.content

        if self.debug:
            print(f"Fetched content from {url}")
        
        return json.loads(content)


    def get(self, url: str) -> dict:
        """ Makes a GET request to the specified URL. """

        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self.fetch, url)
            result = future.result()
            return result
    
    def post(self, url: str, data: dict) -> dict:
        """ Makes a POST request to the specified URL. """

        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(requests.post, url, data=data)
            result = future.result()
            return result.json()
