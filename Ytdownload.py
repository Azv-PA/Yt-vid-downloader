import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog

def download(url, save_path):
    try:
        ydl_opts = {
            'format': 'best',  # Download the best single format (no merging required)
            'outtmpl': save_path + '/%(title)s.%(ext)s',
            'noplaylist': True
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("video downloaded")
    except Exception as e:
        print(e)

url = input("Enter URL to download video: ")
save_path = "C:/Users/User/desktop"
download(url, save_path)
