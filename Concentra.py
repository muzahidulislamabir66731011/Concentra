import time
from gtts import gTTS
import io
import pygame
import speech_recognition as sr
from word2number import w2n

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
    del fp

def word_to_num(word):
    word = word.lower().strip()
    try:
        return float(word)
    except ValueError:
        pass

    try:
        return float(w2n.word_to_num(word))
    except ValueError:
        return None


def get_voice_input(prompt_text="Say the alarm time in minutes"):
    speak_text(prompt_text)
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak_text("Listening")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        speak_text(f"You said {text}")
        return text
    except sr.UnknownValueError:
        speak_text("Sorry, I did not understand. Please try again.")
        return None
    except sr.RequestError:
        speak_text("Sorry, there is a problem with the speech service.")
        return None

def text_alarm():
    speak_text("Hello! I am xyz, your study and focus assistant. I’m here to help you stay focused. Please tell me how many minutes you want to set the alarm for. Just say the number. Thank you!")
    while True:
        user_input = get_voice_input("Set alarm time in minutes")
        if user_input is None:
            continue
        minutes = word_to_num(user_input)
        if minutes is None:
            speak_text("Invalid input. Please say a number.")
            continue
        if minutes <= 0:
            speak_text("Please enter a positive number.")
            continue
        break

    seconds = minutes * 60
    time.sleep(seconds)
    speak_text("Alarm! Time's up!")


if __name__ == "__main__":
    text_alarm()
