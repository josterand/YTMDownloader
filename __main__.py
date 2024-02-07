import customtkinter
import tkinter as tk
from pytube import YouTube

# Download Function
def download():
    try:
        # Get link, select the audio-only streams, and download
        linkObject = YouTube(downloadLinkField.get())
        musicStreams = linkObject.streams.filter(only_audio=True)
        dl = linkObject.streams.get_by_itag(musicStreams.get_audio_only().itag)
        dl.download(output_path="./Music/")
        print("Download Completed")
    except:
        print("The YouTube link is invalid!")

# App Settings
appWindow = customtkinter.CTk()
appWindow.geometry("720x420")
appWindow.title("Youtube Music Downloader by josterand")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
SPOTIFY_GREEN_HEX = "#1DB954"

# Download Link Input Field
urlVar = tk.StringVar()
downloadLinkLabel = customtkinter.CTkLabel(appWindow, text="Insert YouTube link here").pack(padx=10, pady=10)
downloadLinkField = customtkinter.CTkEntry(appWindow, width=400, height=30, textvariable=urlVar)
downloadLinkField.pack()

# Download Button
downloadButton = customtkinter.CTkButton(
    master=appWindow, 
    fg_color=SPOTIFY_GREEN_HEX, 
    text="Download",command=download)
downloadButton.place(
        relx=0.5, 
        rely=0.5, 
        anchor=tk.CENTER
    )

if __name__ == "__main__":
    appWindow.mainloop()