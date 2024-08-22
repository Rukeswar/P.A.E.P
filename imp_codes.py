from all_packages import *
def takeinput(timeout = 5):
    try:
        r = sr.Recognizer()
    except Exception as e:
        print(e)
    with sr.Microphone() as source:
        print("listening..")
        r.phrase_threshold=0.6
        audio = r.listen(source, timeout=timeout, phrase_time_limit=timeout)
        try:
            q=r.recognize_google(audio,language="en-in")
            print(f"user said {q}")
            return q.lower()
        except Exception as e :
            print("speak again")

speaker = win32com.client.Dispatch("SAPI.SpVoice")
def speak(x):
    speaker.Speak(x)

