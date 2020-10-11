# to print all languages that google translator support
import googletrans
#print(googletrans.LANGUAGES)

# importing necessary modules
import speech_recognition as sr
import os
from gtts import gTTS # google text to speech
from googletrans import Translator

# creating recognizer class object 
recog = sr.Recognizer()

# creatign microphone interface
mic = sr.Microphone()

# capturing voice
with mic as source:
    print("speak hello to initiate the translation")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    recog.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog.listen(source)
    mytext = recog.recognize_google(audio)
    mytext = mytext.lower()

# initiating if hello is received from user 
if "hello" in mytext:
    # translator method for translation
    translator = Translator()

    # source and destined language 
    from_lang = 'en'
    to_lang = 'hi'

    # using recognize_google() to convert audio into text
    get_sentence = recog.recognize_google(audio)

    try:

        # printing speech to be translated
        print("phase to be translated :"+get_sentence)

        # using translate method that needs 3 arguments
        # 1st -- sentence to be translated
        # source languge
        # destination language        
        text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)

        # storing translated text into text variable
        text = text_to_translate.text

        # using gTTS() method to speak the translated text
        speak = gTTS(text = text, lang=to_lang,slow=False)

        # using save() method to save translated voice into voice.mp3
        speak.save("voice.mp3")

        #using os module to run the translated voice
        os.system("start voice.mp3")


        
        text = text_to_translate.text

    except sr.UnknownValueError:
        print("Unable to understand the input")

    except sr.RequestError as e:
        print("Unable to provide required output".format(e))
