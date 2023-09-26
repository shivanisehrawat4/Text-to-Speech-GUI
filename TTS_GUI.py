# Importing necessary libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import time

# Initializing the main window
root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='AntiqueWhite')
root.title('Text to Speech Converter')

# Heading
Label(root, text='Convert your Text to Speech', font='arial 12 bold', bg='WhiteSmoke').pack()

# Label for text input
Label(root, text='Enter Text', font='arial 12 bold', bg='WhiteSmoke').place(x=20, y=60)

# Text variable
text_to_convert = StringVar()

# Entry field for user input
entry_field = Entry(root, textvariable=text_to_convert, width='50')
entry_field.place(x=20, y=100)

# Function to convert text to speech
def convert_text_to_speech():
    user_input = entry_field.get()
    speech = gTTS(text=user_input)
    # Generate a unique filename for each conversion
    filename = f"tts_{int(time.time())}.mp3"
    speech.save(filename)
    playsound(filename)
    # Clean up the generated file after playing
    os.remove(filename)

# Function to exit the application
def exit_application():
    root.destroy()

# Function to reset the entry field
def reset_entry_field():
    text_to_convert.set("")

# Creating buttons
Button(root, text="PLAY", font='arial 12 bold', command=convert_text_to_speech, bg='LightBlue', width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 12 bold', command=exit_application, bg='OrangeRed').place(x=100, y=140)
Button(root, text='RESET', font='arial 12 bold', command=reset_entry_field).place(x=175, y=140)

# Infinite loop to run the program
root.mainloop()
