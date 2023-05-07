class Player:
    def __init__(self, elapsed: int, total: int, song_name: str, song_artist: str):
        self.elapsed = elapsed
        self.total = total
        self.song_name = song_name
        self.song_artist = song_artist
    
    def format_time(self, milliseconds):
        """Formates time in milliseconds to minutes and seconds"""
        seconds = milliseconds / 1000
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def generate(self):
        """Generates a progress bar with the elapsed time and total time of the song"""
        bar_length = 30
        progress = self.elapsed / self.total
        filled_length = int(round(bar_length * progress))
        empty_length = bar_length - filled_length

        bar = "━" * filled_length + "●" + "─" * empty_length
        formatted_elapsed = self.format_time(self.elapsed)
        formatted_total = self.format_time(self.total)

        final_bar = f"{formatted_elapsed} {bar} {formatted_total}"
        artist = f"**{self.song_name}** By **{self.song_artist}**"

        message = f"{artist}\n{final_bar}"

        return message