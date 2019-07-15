import pyttsx3

def sp(h):
    engine = pyttsx3.init()
    vol = engine.getProperty('volume')
    engine.setProperty('volume',1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',140)
    engine.say(h)
    engine.runAndWait()
    engine.stop()
    
    
