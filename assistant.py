import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import psutil
from gtts import gTTS
import requests
from bs4 import BeautifulSoup
import subprocess
import pygame


recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.say("This is an example of a female voice.")
engine.runAndWait()
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

def shutdown_computer():
    os.system("shutdown /s /t 1")
    speak("Okay, sir. Shutting down the computer.")

def restart_computer():
    os.system("shutdown /r /t 1")
    speak("Okay, sir. Restarting the computer.")

def open_folder(folder_path):
    subprocess.Popen(f'explorer "{folder_path}"')
    speak("Okay, sir. Opening the folder.")

def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    else:
        return "Battery information not available." 
def blog(request):
    subprocess.Popen("this is a bater start point for cunversactiopn system ")



def get_news(query):
    # Craft the Google search URL based on the user's query
    search_url = f"https://www.google.com/search?q={query}&tbm=nws"
    
    # Send a GET request to Google
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract news headlines from the search results
    headlines = [headline.text for headline in soup.find_all('h3')]
    
    # Extract news summaries if available
    summaries = [summary.text for summary in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')]
    
    # Combine headlines and summaries
    news_articles = [f"{headlines[i]}: {summaries[i]}" for i in range(min(len(headlines), len(summaries)))]
    
    return news_articles

# def text_to_speech(text):
#     # Initialize pygame mixer
#     pygame.mixer.init()

#     # Load the text as a speech
#     tts = gTTS(text=text, lang='hi')  # 'hi' for Hindi
#     tts.save("news.mp3")

#     # Load the speech file and play it
#     pygame.mixer.music.load("news.mp3")
#     pygame.mixer.music.play()

#     # Wait until speech is finished playing
#     while pygame.mixer.music.get_busy():
#         continue

#     # Clean up resources
#     pygame.mixer.quit()


def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Configure the engine to use Hindi language
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('voice', 'hindi')
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_HI-IN_HEERA_11.0')  # Change the voice according to available Hindi voice on your system
    
    # Speak the provided text
    engine.say(text)
    engine.runAndWait()   

def greet():
    speak("Hello, Satish what you want to today?")
    print("Hello, sir. How may I help you?")

def process_command(command):
    print("Received command:", command)  
    if "anu" in command.lower():
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
        elif command.lower() == "shutdown":
            shutdown_computer()
        elif command.lower() == "restart":
            restart_computer()
        elif command.lower().startswith("open folder"):
            folder_path = command[11:].strip()
            os.startfile(folder_path)
            speak(u"ठीक है, सर. फ़ोल्डर खोल रहा हूँ।")
        elif command.lower() == "open file explorer":
            os.system("explorer")
            speak(u"ठीक है, सर. फ़ाइल एक्सप्लोरर खोल रहा हूँ।")
        elif "battery percentage" in command.lower():
            battery_percentage = get_battery_percentage()
            speak(u"सर, बैटरी स्तर {battery_percentage} प्रतिशत है।")
        elif "news" in command.lower():
            language = detect_language(command)  # Function to detect language
            if language == "hi":
                speak(u"आपके लिए खबरें ला रहा हूँ।")
            else:
                speak(u"Bringing you the latest news.")
            main(language)  # Call the main function to fetch and read news articles
        else:
            print(u"क्षमा करें, मुझे आपका आदेश समझ में नहीं आया।")
            speak(u"क्षमा करें, मुझे आपका आदेश समझ में नहीं आया।")
    else:
        print(u"क्षमा करें, मुझे आपका आदेश समझ में नहीं आया।")
        speak(u"क्षमा करें, मुझे आपका आदेश समझ में नहीं आया।")


def detect_language(text):
    """
    Detect the language of the given text.
    """
    # You can use language detection libraries like langdetect or TextBlob for this purpose
    # Here, we are assuming a simple implementation based on the first character
    first_char = text[0].lower()
    if "a" <= first_char <= "z":
        return "en"  # English
    elif "अ" <= first_char <= "ह":
        return "hi"  # Hindi
    else:
        return "en" 

# Greet the user
greet()

# Continuous listening for commands
def main():
    while True:
        command = listen_for_command()
        if command and command == "exit":
            speak("Goodbye, sir.")
            break
        elif command:
            process_command(command)

if __name__ == "__main__":
    main()
