import yt_dlp as youtube_dl #imports the main library used 
import tkinter as tk #i forgot ask bob
from tkinter import filedialog #was gonna include a mp3 but im too lazy ill do it later (that means 10yrs from now if your lucky)

def download(url, save_path): #defines the download function
    try:
        ydl_opts = {
            'format': 'best',  #Downloads the file in the best format
            'outtmpl': save_path + '/%(title)s.%(ext)s', #saves the file to a location
            'noplaylist': True 
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("video downloaded") #pointless remove it you want 
    except Exception as e:
        print(e)

url = input("Enter URL to download video: ") #input for the clip
save_path = "C:/Users/User/desktop" #where the mp4 is saved to
download(url, save_path) #once finised it fully downloads
