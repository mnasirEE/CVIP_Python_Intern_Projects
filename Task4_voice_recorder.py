"""
4. Voice Recorder
The objective of this project is to design and develop a voice recorder application in Python
that allows users to record audio using their device's microphone, save the recordings, and
manage them. The application should provide an intuitive user interface and reliable audio
recording capabilities
"""


from tkinter import *
import tkinter as tk
import sounddevice as sd
import soundfile as sf
from tkinter import filedialog
import os
# from ttkthemes import ThemedTk 
# from ttkthemes import themed_tkinter as ttk
from ttkwidgets import tooltips
root = Tk()
root.title("Nasir's Voice Recorder")
root.geometry("355x255")

f1 = Frame(root)
f1.pack()
# Create a function to show tooltips
def show_tooltip(text):
    tooltip_label.config(text=text)
    tooltip_label.place(x=root.winfo_pointerx() - root.winfo_rootx() + 10, y=root.winfo_pointery() - root.winfo_rooty() + 10)
    
# Create a function to hide tooltips
def hide_tooltip(event):
    tooltip_label.place_forget()

# Buttons
start_img = PhotoImage(file= "start.png")
stop_img = PhotoImage(file= "stop.png")
save_img = PhotoImage(file= "save.png")
play = Button(f1, image= start_img,width=50, height=50,pady = 5)
play.pack(side=LEFT)
stop = Button(f1, image = stop_img, width=50, height=50, pady = 5 )
stop.pack(side= LEFT)
save = Button(f1, image= save_img, width=50, height=50, pady = 5)
save.pack(side=LEFT)
status = StringVar()
status_value = Label(root, textvariable=status)
status_value.pack()

def start_recording():
    global rec_audio
    global sample_rate
    global audio_path
    status.set("Recording...")
    sample_rate = 44100
    duration = 10
    rec_audio = sd.rec(int(duration * sample_rate), samplerate= sample_rate, channels=1)
    # sd.wait()
    # print("recording finished")
    audio_path = True


def stop_recoding():
    status.set("recording stop")
    sd.stop()
def save_recording():
    global rec_audio
    global sample_rate
    global audio_path
    if audio_path:
        file_path = filedialog.asksaveasfilename(defaultextension= ".mp3", filetypes= [( ".mp3 or .wav")])
        if file_path:
            sf.write(file_path, rec_audio, sample_rate)
            status.set("recording saved")
        else:
            status.set("Recording not saved")    
    else:
        status.set("Audio not recorded")
play.config(command= start_recording)
stop.config(command= stop_recoding)
save.config(command=save_recording)
rec_audio = 0
sample_rate = 0
audio_path = False

# Create tooltips for the buttons with icons
play_tooltip_text = "Start Recording"
stop_tooltip_text = "Stop Recording"
save_tooltip_text = "Save Recording"

# Create a tooltip label
tooltip_label = tk.Label(root, text="", bg="lightyellow", borderwidth=1, relief="solid")
tooltip_label.place_forget()
# Bind events to show/hide tooltips
play.bind("<Enter>", lambda event, text=play_tooltip_text: show_tooltip(text))
play.bind("<Leave>", hide_tooltip)
stop.bind("<Enter>", lambda event, text=stop_tooltip_text: show_tooltip(text))
stop.bind("<Leave>", hide_tooltip)
save.bind("<Enter>", lambda event, text=save_tooltip_text: show_tooltip(text))
save.bind("<Leave>", hide_tooltip)

f1.place(relx=0.5, rely=0.5, anchor="center")
root.mainloop()