import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes

# Set Wikipedia language and short summary
wikipedia.set_lang("en")
print("Voice Assistant ready... Speak now!")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print(f"Assistant: {text}")

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
    except:
        return "None"
    return query.lower()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {str_time}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't get that. Try again.")
