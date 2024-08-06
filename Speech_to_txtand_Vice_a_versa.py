import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog
import speech_recognition as sr 
from pygame import mixer

r = sr.Recognizer()
mixer.init()

def recognize_file():
    f = select_file()
    mixer.music.load(f)
    mixer.music.play()
    with sr.AudioFile(f) as sourse:
        audio = r.record(sourse)

        try:
            text.widget.delete('0.0','end')
            text = r.recognize_google(audio)
            text_widget.insert('0.0',text)

        except sr.UnknownValueError:
            print('could not recognize')

        except sr.RequestError as e:
            print(e)

def save_file():
    f = select_file()
    print(f"File path: '{f}'")
    with open(f,'w') as file:
        file.write(text_widget.get('0.0','end'))

def select_file():
    file_path = filedialog.askopenfilename(title = 'select a file')
    return file_path

root = tk.Tk()
root.title('speech to text')

text_widget = tk.Text(font = ('Arial',15))
text_widget.grid(column = 0, row = 0 )

button_frame = tk.Frame()
button_frame.grid(column = 0, row = 1)

recognize_btn = ttk.Button(button_frame, text='recognize', command = recognize_file)
save_btn = ttk.Button(button_frame,text='save_As', command = save_file)

recognize_btn.grid(column = 0, row = 0)
save_btn.grid(column = 1 , row = 0)

root.mainloop()