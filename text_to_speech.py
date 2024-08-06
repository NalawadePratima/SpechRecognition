import tkinter as tk
from tkinter import ttk
import pyttsx3 as tts

engine = tts.init()

def text_to_speech():
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice',voices[0].id)
    
    engine.setProperty('rate', 150)
    
    engine.setProperty('volume',1)

    t = text.get('0.0','end')
    engine.say(t)
    engine.runAndWait()

def save():
    t = text.get('0.0','end')
    engine.save_to_file(t,'text.mp3')
    engine.runAndWait()


root = tk.Tk()
root.title('text to speech')

text =tk.Text(font=('Arial',15))
text.grid(column=0,row=0)

button_frame=tk.Frame()
button_frame.grid(column = 0,row = 1)

say_btn = ttk.Button(button_frame,text='say',command=text_to_speech)
save_btn = ttk.Button(button_frame,text='save',command=save)

say_btn.grid(column=0,row=0)
save_btn.grid(column=1,row=0)

root.mainloop()
