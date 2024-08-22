from all_packages import *
from functions import *
from imp_codes import *
from database import *
from switchcase import *


if __name__ =='__main__':
    while 1:
        try:
            r = takeinput()

            if "wake up" in r.lower():
                print("hello")

                speaker.Speak("hi ,HELLO i am Jarvis how can i help you today??")
                while 1:
                    try:
                        print("hi")
                        y = takeinput()
                        switchcase(y)
                        if "terminate" in y.lower():
                            speak("ok bye bye ta ta see you , love you so much , okay , signing off,")
                            break
                        if y.lower() == "nothing":
                            speak("ok")
                            break
                    except Exception as e:
                        print(e)
                        print("again")
                        speak("please repeat again!!")
        except Exception as e:
            print(e)