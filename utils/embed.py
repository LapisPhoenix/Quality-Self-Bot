import aiohttp
import urllib.parse


class Embed:
    """Basic Embed working with https://embed.rauf.workers.dev/"""
    def __init__(self, title: str, description: str, color: str = "6551FF", url: str = "https://www.discord.com"):
        self.title = title
        self.description = description
        self.color = color
        self.url = url
        self.base = "https://embed.rauf.workers.dev/?"
        self.hide_text = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
    

    async def URL_SAFE(self, text):
        """Encode the URL to be URL safe"""
        # Encode the URL
        encoded_url = urllib.parse.quote_plus(text)
        # Replace '+' with '%20' and '%' with '%25'
        uri_safe_string = encoded_url.replace('+', '%20').replace('%', '%25')
        return uri_safe_string
    

    async def generate(self) -> str:
        URL_SAFE_TITLE = await self.URL_SAFE(text=self.title)
        URL_SAFE_DESCRIPTION = await self.URL_SAFE(text=self.description)
        URL_SAFE_REDIRECT = await self.URL_SAFE(text=self.url)

        return f"{self.hide_text}{self.base}title={URL_SAFE_TITLE}&description={URL_SAFE_DESCRIPTION}&color={self.color}&redirect={URL_SAFE_REDIRECT}"
