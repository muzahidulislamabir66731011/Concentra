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


def get_voice_input(prompt_text="When should I remind you"):
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
        speak_text("Sorry, I did not understand. Please type the minutes using letters, not numbers.")
        return input("Type your time: ")
    except sr.RequestError:
        speak_text("Sorry, there is a problem with the speech service.Please type the minutes using letters, not numbers.")
        return input("Type your time: ")

def text_alarm():
    speak_text("Hello! I am Concentra, your study and focus assistant. I am here to help you stay focused. Please tell me how many minutes you want to set the alarm for. Just say the number. Thank you!")

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

    original_minutes = minutes

    while True:
        seconds = minutes * 60
        time.sleep(seconds)

        speak_text("Hey, time's up! Do you want to continue with the same timer or stop?")
        speak_text("Say 'stop' to end, or say nothing to continue.")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = None
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=4)  
            except sr.WaitTimeoutError:
                minutes = original_minutes
                continue

        try:
            response = r.recognize_google(audio).lower().strip()
            if "stop" in response:
                speak_text("Okay, stopping the alarm. Have a great day!")
                break
            elif response == "":
                minutes = original_minutes
            else:
                new_time = word_to_num(response)
                if new_time is not None and new_time > 0:
                    minutes = new_time
                    original_minutes = new_time
                else:
                    minutes = original_minutes
        except sr.UnknownValueError:
            minutes = original_minutes
        except sr.RequestError:
            speak_text("There was an error with the speech service. Continuing with same timer.")
            minutes = original_minutes


if __name__ == "__main__":
    text_alarm()
