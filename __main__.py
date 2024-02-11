import tkinter as tk
import customtkinter
from pytube import YouTube
from pytube import exceptions
from urllib import error

APP_VERSION = "v2.2.2"
APP_ACCENT_COLOR = "#006191" # Blue

# Light & Dark Colors
RED_COLORS = ["#FF0000", "#FF5D5D"]
GREEN_COLORS = ["#08A300", "#61FF58"]
YTM_LINK = "https://music.youtube.com/watch?v="

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure app window
        self.geometry("620x420")
        self.resizable(False, False)
        self.title(f"YTM Downloader {APP_VERSION} by Josterand")
        self.appearance_mode = customtkinter.set_appearance_mode("Dark")
        self.default_color_theme = customtkinter.set_default_color_theme("dark-blue")

        # Configure UI
        url_var = tk.StringVar()
        self.url_label = customtkinter.CTkLabel(self, text="Insert a valid YouTube Music link")
        self.url_label.pack(padx=10, pady=10)
        self.url_label.place(relx=0.5, rely=0.10, anchor=tk.CENTER)
        self.url_field = customtkinter.CTkEntry(self, width=400, height=30, textvariable=url_var)
        self.url_field.pack()
        self.url_field.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

        # Download Button
        self.download_button = customtkinter.CTkButton(self, fg_color=APP_ACCENT_COLOR,text="Download Now", corner_radius=150, command=self.download)
        self.download_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # In-App Logging 
        self.log_box = customtkinter.CTkTextbox(self, state="normal", width=500, height=80, border_width=2.5, activate_scrollbars=False)
        self.log_box.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.log("App started")

        # Status Label
        self.status_label = customtkinter.CTkLabel(self, corner_radius=150, text="")
        self.status_label.pack(padx=10, pady=10)
        self.status_label.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

    def log(self, text:str):
        all_log = self.log_box.get("0.0", "end")
        log = str("[LOG-INFO] " + text + "\n" + all_log)
        self.log_box.delete("0.0", "end")
        self.log_box.insert("0.0", log)
    
    def check_link(self, link:str):
        self.log("Checking the link provided...")
        if YTM_LINK in link:
            self.log("Link OK!")
            return True
        else:
            self.log("Link error!")
            return False

    def download(self):
        if not self.check_link(self.url_field.get()):
            self.log("Error! The link given is not a YouTube music link!")
            self.status_label.configure(
                text_color=RED_COLORS,
                text="This link is not a YouTube Music Link"
            )
        else:
            try:
                self.log("Getting music information from YouTube...")
                link_object = YouTube(self.url_field.get())
                music_title = link_object.title
                self.log("Getting streams...")
                audio_streams = link_object.streams.filter(only_audio=True)
                self.log("Getting audio streams...")
                dl = audio_streams.get_by_itag(audio_streams.get_audio_only().itag)
                self.log("Starting download...")
                dl.download(output_path="./Music/", filename=music_title + ".mp3")

                # Log 
                self.log("Download success")
                self.status_label.configure(
                    text_color=GREEN_COLORS,
                    text="Download Success!",
                )
            except exceptions.RegexMatchError:
                self.log("Error occured! (RegexMatchError)")
                self.status_label.configure(
                    text_color=RED_COLORS,
                    text="Invalid link! Download failed!"
                )
            except exceptions.AgeRestrictedError:
                self.log("Error occured! (AgeRestrictedError)")
                self.status_label.configure(
                    text_color=RED_COLORS,
                    text="This link is age resticted! Download failed!"
                )
            except exceptions.VideoRegionBlocked:
                self.log("Error occured! (VideoRegionBlocked)")
                self.status_label.configure(
                    text_color=RED_COLORS,
                    text="This content is region restricted! Download failed!"
                )
            except error.URLError:
                self.log("Error occured! (URLError)")
                self.status_label.configure(
                    text_color=RED_COLORS,
                    text="Try checking your connection! Download failed!"
                )
            except:
                self.log("Error occured!")
                self.status_label.configure(
                    text_color=RED_COLORS,
                    text="Download failed!"
                ) 

app = App()
app.mainloop() 
