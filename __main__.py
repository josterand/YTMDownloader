import time
import tkinter as tk
from pytube import YouTube
from customtkinter import (
    CTk,
    CTkButton,
    CTkLabel,
    CTkEntry,
    CTkTextbox,
    set_appearance_mode,
    set_default_color_theme,
)

YTM_LINK = "https://music.youtube.com/watch?"
APP_ACCENT_COLOR = "#006191"
appWindow = CTk()
appWindow.geometry("720x420")
appWindow.resizable(False, False)
appWindow.title("Youtube Music Downloader by josterand")
set_appearance_mode("Dark")
set_default_color_theme("dark-blue")

def logging(logText:str):
    time.sleep(0.5)
    allLog = textbox.get("0.0", "end")
    log = "[INFO-APP] " + logText + "\n" + allLog
    textbox.delete("0.0", "end")
    textbox.insert("0.0", log)

def checkLink(link:str):
    logging("Checking the given link")
    if YTM_LINK in link:
        logging("Link OK")
        return True
    else:
        logging("Link error!")
        return False

def download():
    if checkLink(linkField.get()):
        try:
            # Getting The Audio Only Stream
            logging("Getting music information from youtube")
            linkObject = YouTube(linkField.get())
            logging("Getting streams")
            musicStreams = linkObject.streams.filter(only_audio=True)
            logging("Getting audio streams")
            dl = linkObject.streams.get_by_itag(musicStreams.get_audio_only().itag)
            logging("Downloading music")
            dl.download(output_path="./Music/")

            # Log & Notification
            finishedLabel.configure(
                text_color=["#08A300", "#61FF58"], # Light & Dark Colors
                text="Downloaded",
            )
            logging("Download success")
        except:
            logging("Error occured!")
            finishedLabel.configure(
                text_color=["#FF0000", "#FF5D5D"], # Light & Dark Colors
                text="Download Failed!"
            )
    else:
        logging("Error! The given link is not a youtube music link")
        finishedLabel.configure(
            text_color=["#FF0000", "#FF5D5D"], # Light & Dark Colors
            text="This link is not a Youtube Music Link"
        )

# Notification Labels To Inform User If Its Success Or Error
finishedLabel = CTkLabel(appWindow, corner_radius=150, text="")
finishedLabel.pack(padx=10, pady=10)
finishedLabel.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

# Download Link Input Field
urlVar = tk.StringVar()
linkLabel = CTkLabel(appWindow, text="Insert a valid Youtube Music link")
linkLabel.pack(padx=10, pady=10)
linkLabel.place(relx=0.5, rely=0.10, anchor=tk.CENTER)

linkField = CTkEntry(appWindow, width=400, height=40, textvariable=urlVar)
linkField.pack()
linkField.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

# Download Button
downloadButton = CTkButton(
    master=appWindow, 
    fg_color=APP_ACCENT_COLOR, 
    text="Download Now", 
    command=download, 
    corner_radius=150
)
downloadButton.place(
    relx=0.5, 
    rely=0.4, 
    anchor=tk.CENTER
)

# Text-Box For In-App Logging
textbox = CTkTextbox(
    master=appWindow, 
    state="normal", 
    width=600, 
    height=90,
    border_width=2.5,
    activate_scrollbars=False,
)
textbox.place(
    relx=0.5, 
    rely=0.8, 
    anchor=tk.CENTER)
textbox.insert("0.0", "[INFO-APP] App started")

if __name__ == "__main__":
    appWindow.mainloop()