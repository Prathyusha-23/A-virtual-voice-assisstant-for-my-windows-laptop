import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import google.generativeai as genai

# 🔑 Set your full Gemini API Key here (from https://makersuite.google.com/app/apikey)
GENAI_API_KEY = "AIzaSyAgR3Xp-NcLjuOxffI-f1i15E_s39XNuAQ"  # 🔁 Replace this with your actual full key
genai.configure(api_key=GENAI_API_KEY)

# Create Gemini model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()  # Start chat session for ongoing prompts

# 🗣️ Text-to-Speech Setup
engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # [0]=male, [1]=female

def speak(text):
    print(f"🗣️ Windows: {text}")
    engine.say(text)
    engine.runAndWait()

# 🎧 Voice Input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"👤 You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Voice recognition service is not available.")
        return ""

# 🧠 Ask Gemini
def ask_gemini(prompt):
    try:
        print(f"📨 Sending prompt to Gemini: {prompt}")
        response = chat.send_message(prompt)
        print("✅ Gemini response received")
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini Error: {e}")
        return "Sorry, I couldn't reach Gemini."

# 🧩 Command Handler

def handle_command(command):
    if "hey windows open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")

    elif "hey windows open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")

    elif "hey windows open notepad" in command:
            os.system("notepad")
            speak("Opening Notepad.")

    elif "hey windows open vs code" in command:
            os.startfile("C:\\Users\\User\\OneDrive\\Desktop\\Visual Studio Code.lnk")  # Update if needed
            speak("Opening Visual Studio Code.")

    elif "hey windows open word" in command:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")
            speak("Opening Microsoft Word.")
    elif "hey windows open excel" in command:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")
            speak("Opening Microsoft Excel.")
    elif "hey windows open powerpoint" in command:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")
            speak("Opening PowerPoint.")

    elif "hey windows open power bi" in command:
            os.startfile("C:\\Program Files\\Microsoft Power BI Desktop\\bin\\PBIDesktop.exe")
            speak("Opening Power BI.")

    elif "hey windows close vs code" in command:
            os.system("taskkill /f /im Code.exe")
            speak("Closing Visual Studio Code.")

    elif "hey windows close word" in command:
            os.system("taskkill /f /im WINWORD.EXE")
            speak("Closing Microsoft Word.")

    elif "hey windows close excel" in command:
            os.system("taskkill /f /im EXCEL.EXE")
            speak("Closing Microsoft Excel.")

    elif "hey windows close powerpoint" in command:
            os.system("taskkill /f /im POWERPNT.EXE")
            speak("Closing PowerPoint.")

    elif "hey windows close power bi" in command:
            os.system("taskkill /f /im PBIDesktop.exe")
            speak("Closing Power BI.")

    elif "hey windows what is the time right now" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

    elif "hey windows what is today's date" in command:
            date = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today is {date}")

    elif "hey windows tell me a joke" in command:
            speak("Why don't scientists trust atoms? Because they make up everything!")

    elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye!")
            exit()

    else:
            answer = ask_gemini(command)
            speak(answer)
# 🚀 Main Assistant Loop
if __name__ == "__main__":
    speak("Hello prathyusha, I am windows your virtual AI assistant for your laptop. How can I help you?")

    while True:
        command = listen()
        if command:
            handle_command(command)