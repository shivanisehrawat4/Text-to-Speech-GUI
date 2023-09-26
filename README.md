# Text to Speech Converter

## Overview
This Python code creates a graphical user interface (GUI) application for converting text to speech using the **gTTS (Google Text-to-Speech)** library. The application allows users to enter text, convert it to speech, play the speech, and optionally save the generated speech as an audio file. The application is built using the **tkinter** library for the GUI, **gTTS** for text-to-speech conversion, and **playsound** for audio playback.

## Dependencies
To run this application, you need the following libraries:

- **tkinter** library (for GUI)
- **gTTS (Google Text-to-Speech)** library (for text-to-speech conversion)
- **playsound** library (for audio playback)
- **os** library (for file operations)
- **time** library (for generating unique audio filenames)

## Application Components

### 1. Main Window
- The main window is initialized using the Tk() constructor and is configured with a specific size, background color, and title.
- It is set to be non-resizable.

### 2. Heading
- A title label, "**Convert Text to Speech**," is displayed at the top of the window.

### 3. Text Input Field
- A label "**Enter Text**" is displayed above an entry field where the user can input the text they want to convert to speech.
- The user's input is stored in the **text_to_convert** variable of type StringVar().

### 4. Buttons
- **PLAY Button**: When clicked, it calls the **convert_text_to_speech()** function to convert the user's input text to speech. The generated speech is played, and a unique audio file is created for each conversion.
- **EXIT Button**: When clicked, it calls the **exit_application()** function to close the application.
- **RESET Button**: When clicked, it calls the **reset_entry_field()** function to clear the text input field.

### 5. Functions

#### **convert_text_to_speech()**
- Retrieves the text entered by the user from the input field.
- Uses the **gTTS** library to convert the text to speech and generates a unique filename for the audio file.
- Saves the generated speech as an MP3 audio file.
- Plays the generated audio using the **playsound** library.
- Cleans up by removing the temporary audio file after playback.

#### **exit_application()**
- Destroys the main window, effectively closing the application.

#### **reset_entry_field()**
- Clears the text input field by resetting the **text_to_convert** variable.

## How to Use
1. Run the script, and the application window will appear.
2. Enter the text you want to convert to speech in the input field.
3. Click the "**PLAY**" button to convert and play the speech.
4. Optionally, you can click the "**EXIT**" button to close the application or the "**RESET**" button to clear the input field for new text input.

## Notes
- Each time the "**PLAY**" button is clicked, a unique audio file is generated with a timestamp to prevent overwriting previous conversions.
- The temporary audio file is deleted after it is played to save disk space.
- The application runs in an infinite loop (`root.mainloop()`) to keep the GUI responsive until the user closes the window.
