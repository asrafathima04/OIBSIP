# Voice Assistant by Asra Fathima 🌷
# Beginner version using text input instead of microphone

import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')

def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    command = input("You: ").lower()
    return command

def run_asra():
    talk("Hi, I am your voice assistant Asra!")
    while True:
        command = listen()

        if "hello" in command:
            talk("Hello Asra! Nice to hear from you.")
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk("The current time is " + time)
        elif "date" in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            talk("Today's date is " + date)
        elif "search" in command:
            talk("What should I search for?")
            query = listen()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            talk("Here are your search results.")
        elif "exit" in command or "bye" in command:
            talk("Goodbye Asra! Have a nice day!")
            break
        else:
            talk("Sorry, I didn't understand that. Please try again.")

run_asra()