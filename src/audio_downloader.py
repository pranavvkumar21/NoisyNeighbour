#!/usr/bin/env python3
import yt_dlp
import os, requests
url = 'https://www.youtube.com/watch?v=0sMPkL8CD_w'


class AudioDownloader:
    def __init__(self, download_path="../data"):
        self.url = None
        self.download_path = download_path
        outtmpl = os.path.join(download_path, '%(title)s/%(title)s.%(ext)s')
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # or 'wav', 'm4a'
                'preferredquality': '192',
            }],
        }
        self.ydl = yt_dlp.YoutubeDL(self.ydl_opts)

    def download_audio(self, url):
        self.url = url
        try:
            info = self.ydl.extract_info(self.url, download=False)

            self.ydl.download([self.url])
            title = info['title']
            thumb_url = info['thumbnail']
            print("Title:", info['title'])
            print("Thumbnail:", info['thumbnail'])
            resp = requests.get(thumb_url)
            with open(f'{self.download_path}/{title}/{title}.jpg', 'wb') as f:
                f.write(resp.content)
        except Exception as e:
            print(f"Error downloading audio: {e}")

if __name__ == "__main__":
    downloader = AudioDownloader()
    downloader.download_audio(url)
    print("Audio downloaded successfully.")