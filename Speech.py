import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Say some thing')
    audio = r.listen(source)
    print('Done!')
    try:
        print("Sphinx :" + r.recognize_sphinx(audio))
    except:
        pass
    try:
        print("Google :" + r.recognize_google(audio))
    except:
        pass

