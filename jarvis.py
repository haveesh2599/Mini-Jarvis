import os
import re
import time
import ctypes
import datetime
import webbrowser

import pyautogui
import pyttsx3
import speech_recognition as sr

from dotenv import load_dotenv
from google import genai

from pycaw.pycaw import AudioUtilities


# ============================================================
# GEMINI SETUP
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key was not found.")
    print("Make sure your .env file contains:")
    print("GEMINI_API_KEY=your_api_key")
    exit()

try:
    client = genai.Client(api_key=api_key)

    chat = client.chats.create(
        model="gemini-3.7-flash"
    )

except Exception as e:
    print("ERROR: Could not connect to Gemini.")
    print(e)
    exit()


# ============================================================
# TEXT TO SPEECH
# ============================================================

def speak(text):

    print("Jarvis:", text)

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)

        engine.say(text)
        engine.runAndWait()

        engine.stop()

    except Exception as e:
        print("Text-to-speech error:", e)


# ============================================================
# SPEECH RECOGNITION
# ============================================================

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def take_command():

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:
                audio = recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=15
                )

            except sr.WaitTimeoutError:
                print("No speech detected.")
                return ""

        print("Recognizing...")

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text.lower().strip()

    except sr.UnknownValueError:

        print("Could not understand the speech.")
        return ""

    except sr.RequestError as e:

        print("Speech recognition service error:", e)

        speak(
            "There was a problem with the speech "
            "recognition service."
        )

        return ""

    except Exception as e:

        print("Microphone error:", e)

        return ""


# ============================================================
# GEMINI AI
# ============================================================

def ask_gemini(question):

    for attempt in range(3):

        try:

            print("\nAsking Gemini...")

            response = chat.send_message(question)

            if response.text:

                return response.text.strip()

            return "I received an empty response from Gemini."

        except Exception as e:

            error_text = str(e)

            print(
                f"Gemini error "
                f"(attempt {attempt + 1}/3):"
            )

            print(error_text)

            # Gemini temporarily overloaded
            if "503" in error_text:

                if attempt < 2:

                    wait_time = 2 ** attempt

                    print(
                        f"Gemini is busy. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:

                    return (
                        "Gemini is currently busy. "
                        "Please try again in a moment."
                    )

            else:

                return (
                    "Sorry, I couldn't connect "
                    "to Gemini right now."
                )

    return "Sorry, I couldn't get a response from Gemini."


# ============================================================
# GET WINDOWS AUDIO DEVICE
# ============================================================

def get_audio_device():

    try:

        devices = AudioUtilities.GetSpeakers()

        return devices.EndpointVolume

    except Exception as e:

        print("Audio device error:", e)

        return None


# ============================================================
# GET CURRENT VOLUME
# ============================================================

def get_volume():

    volume = get_audio_device()

    if volume is None:
        return None

    try:

        current = volume.GetMasterVolumeLevelScalar()

        return round(current * 100)

    except Exception as e:

        print("Could not read volume:", e)

        return None


# ============================================================
# SET EXACT VOLUME
# ============================================================

def set_volume(percent):

    percent = max(0, min(100, percent))

    volume = get_audio_device()

    if volume is None:

        speak("I couldn't control the system volume.")

        return

    try:

        volume.SetMasterVolumeLevelScalar(
            percent / 100,
            None
        )

        speak(
            f"Volume set to {percent} percent."
        )

    except Exception as e:

        print("Volume error:", e)

        speak(
            "Sorry, I couldn't change the volume."
        )


# ============================================================
# INCREASE VOLUME
# ============================================================

def increase_volume(amount):

    current = get_volume()

    if current is None:

        speak("I couldn't read the current volume.")

        return

    new_volume = min(
        100,
        current + amount
    )

    set_volume(new_volume)


# ============================================================
# DECREASE VOLUME
# ============================================================

def decrease_volume(amount):

    current = get_volume()

    if current is None:

        speak("I couldn't read the current volume.")

        return

    new_volume = max(
        0,
        current - amount
    )

    set_volume(new_volume)


# ============================================================
# SCREENSHOT
# ============================================================

def take_screenshot():

    try:

        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        filename = (
            f"jarvis_screenshot_{timestamp}.png"
        )

        screenshot = pyautogui.screenshot()

        screenshot.save(filename)

        speak(
            "Screenshot taken and saved."
        )

        print(
            "Screenshot saved as:",
            filename
        )

    except Exception as e:

        print("Screenshot error:", e)

        speak(
            "Sorry, I couldn't take the screenshot."
        )


# ============================================================
# OPEN APPLICATION
# ============================================================

def open_application(command):

    if "calculator" in command:

        speak("Opening Calculator")

        os.system("start calc")

        return True

    if "notepad" in command:

        speak("Opening Notepad")

        os.system("start notepad")

        return True

    if "file explorer" in command:

        speak("Opening File Explorer")

        os.system("start explorer")

        return True

    if "explorer" in command:

        speak("Opening File Explorer")

        os.system("start explorer")

        return True

    if "vs code" in command:

        speak("Opening Visual Studio Code")

        os.system("start code")

        return True

    if "visual studio code" in command:

        speak("Opening Visual Studio Code")

        os.system("start code")

        return True

    if "chrome" in command:

        speak("Opening Chrome")

        os.system("start chrome")

        return True

    return False


# ============================================================
# START JARVIS
# ============================================================

speak(
    "Hello! I am Jarvis, your personal assistant."
)

speak(
    "How can I help you?"
)


# ============================================================
# MAIN COMMAND LOOP
# ============================================================

while True:

    command = take_command()

    if not command:
        continue


    # ========================================================
    # STOP JARVIS
    # ========================================================

    if (
        command == "stop jarvis"
        or command == "exit jarvis"
        or command == "quit jarvis"
        or command == "goodbye jarvis"
    ):

        speak(
            "Goodbye. See you later."
        )

        break


    # ========================================================
    # TIME
    # ========================================================

    elif (
        command == "time"
        or "what time is it" in command
        or "tell me the time" in command
        or "current time" in command
    ):

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is {current_time}."
        )


    # ========================================================
    # DATE
    # ========================================================

    elif (
        command == "date"
        or "what is the date" in command
        or "today's date" in command
        or "todays date" in command
        or "what day is it" in command
    ):

        current_date = datetime.datetime.now().strftime(
            "%d %B %Y"
        )

        current_day = datetime.datetime.now().strftime(
            "%A"
        )

        speak(
            f"Today is {current_day}, "
            f"{current_date}."
        )


    # ========================================================
    # YOUTUBE
    # ========================================================

    elif (
        "open youtube" in command
        or "go to youtube" in command
    ):

        speak("Opening YouTube")

        webbrowser.open(
            "https://www.youtube.com"
        )


    # ========================================================
    # GOOGLE
    # ========================================================

    elif (
        "open google" in command
        or "go to google" in command
    ):

        speak("Opening Google")

        webbrowser.open(
            "https://www.google.com"
        )


    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    elif command.startswith("search for "):

        search_query = command.replace(
            "search for ",
            "",
            1
        ).strip()

        if search_query:

            speak(
                f"Searching Google for {search_query}"
            )

            url = (
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )

            webbrowser.open(url)

        else:

            speak(
                "What would you like me to search for?"
            )


    elif command.startswith("google "):

        search_query = command.replace(
            "google ",
            "",
            1
        ).strip()

        if search_query:

            speak(
                f"Searching Google for {search_query}"
            )

            url = (
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )

            webbrowser.open(url)


    # ========================================================
    # OPEN APPLICATIONS
    # ========================================================

    elif (
        "open calculator" in command
        or "open notepad" in command
        or "open file explorer" in command
        or "open explorer" in command
        or "open vs code" in command
        or "open visual studio code" in command
        or "open chrome" in command
    ):

        open_application(command)


    # ========================================================
    # SET EXACT VOLUME
    # ========================================================

    elif (
        "set volume to" in command
        or "set the volume to" in command
        or "volume to" in command
    ):

        numbers = re.findall(
            r"\d+",
            command
        )

        if numbers:

            percent = int(numbers[0])

            set_volume(percent)

        else:

            speak(
                "Please tell me the volume percentage."
            )


    # ========================================================
    # INCREASE VOLUME BY NUMBER
    # ========================================================

    elif (
        "increase volume by" in command
        or "increase the volume by" in command
        or "turn volume up by" in command
        or "turn the volume up by" in command
        or "raise volume by" in command
    ):

        numbers = re.findall(
            r"\d+",
            command
        )

        if numbers:

            amount = int(numbers[0])

            increase_volume(amount)

        else:

            speak(
                "Please tell me how much to increase "
                "the volume."
            )


    # ========================================================
    # DECREASE VOLUME BY NUMBER
    # ========================================================

    elif (
        "decrease volume by" in command
        or "decrease the volume by" in command
        or "turn volume down by" in command
        or "turn the volume down by" in command
        or "lower volume by" in command
    ):

        numbers = re.findall(
            r"\d+",
            command
        )

        if numbers:

            amount = int(numbers[0])

            decrease_volume(amount)

        else:

            speak(
                "Please tell me how much to decrease "
                "the volume."
            )


    # ========================================================
    # NORMAL VOLUME UP
    # ========================================================

    elif (
        command == "volume up"
        or command == "increase volume"
        or command == "increase the volume"
        or command == "turn volume up"
        or command == "turn the volume up"
    ):

        increase_volume(5)


    # ========================================================
    # NORMAL VOLUME DOWN
    # ========================================================

    elif (
        command == "volume down"
        or command == "decrease volume"
        or command == "decrease the volume"
        or command == "turn volume down"
        or command == "turn the volume down"
    ):

        decrease_volume(5)


    # ========================================================
    # MUTE
    # ========================================================

    elif (
        command == "mute"
        or command == "mute volume"
        or command == "mute the volume"
    ):

        volume = get_audio_device()

        if volume:

            try:

                volume.SetMute(1, None)

                speak("Volume muted.")

            except Exception as e:

                print("Mute error:", e)

                speak(
                    "Sorry, I couldn't mute the volume."
                )

        else:

            speak(
                "I couldn't control the volume."
            )


    # ========================================================
    # UNMUTE
    # ========================================================

    elif (
        command == "unmute"
        or command == "unmute volume"
        or command == "unmute the volume"
    ):

        volume = get_audio_device()

        if volume:

            try:

                volume.SetMute(0, None)

                speak("Volume unmuted.")

            except Exception as e:

                print("Unmute error:", e)

                speak(
                    "Sorry, I couldn't unmute the volume."
                )

        else:

            speak(
                "I couldn't control the volume."
            )


    # ========================================================
    # CURRENT VOLUME
    # ========================================================

    elif (
        "what is the volume" in command
        or "what's the volume" in command
        or "current volume" in command
        or "tell me the volume" in command
    ):

        current = get_volume()

        if current is not None:

            speak(
                f"The current volume is {current} percent."
            )

        else:

            speak(
                "I couldn't determine the current volume."
            )


    # ========================================================
    # SCREENSHOT
    # ========================================================

    elif (
        "take a screenshot" in command
        or "take screenshot" in command
        or command == "screenshot"
        or "capture my screen" in command
        or "capture the screen" in command
    ):

        take_screenshot()


    # ========================================================
    # LOCK COMPUTER
    # ========================================================

    elif (
        "lock my computer" in command
        or "lock the computer" in command
        or command == "lock computer"
        or command == "lock my pc"
        or command == "lock pc"
    ):

        speak(
            "Locking your computer."
        )

        time.sleep(1)

        ctypes.windll.user32.LockWorkStation()


    # ========================================================
    # GEMINI AI
    # ========================================================

    else:

        answer = ask_gemini(command)

        speak(answer)