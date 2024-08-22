from functions import *
def switchcase(text):
    if "open" in text.lower():
        web(text)
    elif "details" in text.lower():
        getname()
    elif "music" in text.lower():
        music()
    else:
        basicsh(text)
        compliment(text)
        list(text)
        bad(text)