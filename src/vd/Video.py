from pathlib import Path

from yt_dlp import YoutubeDL


class Video:
    def __init__(self, url):
        self.url = url

    def download(self, local_path):
        destination = Path(local_path).expanduser()
        destination.parent.mkdir(parents=True, exist_ok=True)
        options = {
            "noplaylist": True,
            "outtmpl": str(destination),
        }
        with YoutubeDL(options) as downloader:
            downloader.download([self.url])
