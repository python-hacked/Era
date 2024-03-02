import speech_recognition as sr
import webbrowser
import os
import pyttsx3

recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_youtube():
    webbrowser.open("https://www.youtube.com/")
    speak("Okay, sir. Opening YouTube.")

def search_and_play_song(song_name):
    url = f"https://www.youtube.com/results?search_query={song_name}"
    webbrowser.open(url)
    speak("Okay, sir. Searching and playing the song.")

def close_youtube():
    os.system("taskkill /im chrome.exe /f")
    speak("Okay, sir. Closing YouTube.")

def stop_playing_song():
    os.system("taskkill /im chrome.exe /f")
    speak("Okay, sir. Stopping the song.")

def greet():
    speak("Hello, sir. How may I help you?")

def process_command(command):
    if command.lower().startswith("jarvis"):
        command = command[6:].strip()
        print("Executing command:", command)
        if command.lower() == "open youtube":
            open_youtube()
        elif command.lower().startswith("play song"):
            song_name = command[9:].strip()
            search_and_play_song(song_name)
        elif command.lower() == "close youtube":
            close_youtube()
        elif command.lower() == "stop this song":
            stop_playing_song()
        else:
            print("Sorry, I didn't understand the command.")
    else:
        print("Sorry, I didn't hear my name.")

# Greet the user
greet()

# Continuous listening for commands
def main():
    while True:
        command = listen_for_command()
        if command and command.lower() == "exit":
            speak("Goodbye, sir.")
            break
        elif command:
            process_command(command)

if __name__ == "__main__":
    main()
