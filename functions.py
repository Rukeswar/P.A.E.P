from all_packages import *
from imp_codes import *
from database import *
def web(u):
    browsers={"youtube":"https://youtube.com","google":"https://google.com"}
    for i in browsers:
        if i in u.lower():
            webbrowser.open(browsers[i])
            speaker.Speak(f"opening {i}")
def getname():
        speak("say the first name of the person that you need details of!")
        dd=takeinput()
        person_details(dd)

def person_details(x):
    try:
        for i in persons :
            if i == x:
                details=persons[i]
                sen=f"well {i} is a lazy boy. his age is {details[1]}, his full name is{details[0]}, his contact number is {details[2]}"
                speak(sen)
    except Exception as e:
        print("no such person")
        speak("there is no such person name in my database")
def list(c):
    for i in data:
        if c.lower()==i:
            for j in i:
                speak(j)
def compliment(c):
    for i in compliments:
        if i in c.lower():
            speak("aww thankyou for your compliment!!")
def bad(f):
    for i in unparliamentary:
        if i.lower() in f.lower():
            speak(
                "you are a bad person, is this the way to talk to a woman? what do you think of me? i am a grown woman, learn some manners you , get lost!!")
def basicsh(h):
    for i in basics:
        if i.lower() in h:
            speak(basics[i])
def music(song_name=None):
    if song_name:
        search_query = song_name.replace(' ', '+')
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
        speak(f"Playing {song_name} on YouTube")
    else:
        speak("Please provide a song name to play on YouTube")