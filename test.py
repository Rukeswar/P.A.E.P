import speech_recognition as sr

def listen_for_seconds(seconds):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for 5 seconds...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=seconds, phrase_time_limit=seconds)
            print("Processing...")
            try:
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return ""
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""

if __name__ == "__main__":
    listen_for_seconds(5)  # Listen for 5 seconds
