#from gtts import gTTS
#import os
import openai
import speech_recognition as sr
import pyttsx3
import configparser

config = configparser.ConfigParser()
config.read('application.settings')


openai.api_key = config.get('OPENAI', 'OPEN_API_KEY')
CHAT_GPT_MODEL = config.get('OPENAI', 'OPEN_API_KEY')



messages = []
def send_to_chatGPT(messages, model=CHAT_GPT_MODEL):
    response = openai.ChatCompletion.create(
        model=messages
    )

    message =response.choices[0].message.content
    messages.appened(response.choices[0].message)
    return message 


r = sr.Recognizer()

def speak_text(command):
    print("Attempting to speak...")
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        #engine.setProperty('voices', voices[1].id)
        engine.say(command)
        print("Said: " + command)
        engine.runAndWait()
    except:
        e = sys.exec_info()[0]
        print(e)
def get_input_from_user(source2):
    r.adjust_for_ambient_noise(source2, duration=0.2)
    audio2 = r.listen(source2)
    my_text =r.recognize_google(audio2)
    
    my_text = my_text.lower()
    print("cmmand: " + my_text)
    return my_text

while(1):
    try:
        cont = 0
        with sr.Microphone() as source2:
            my_text = get_input_from_user(source2)
            print("Command: " + my_text) 
            #text = "My Name is Alyssa"
            if my_text == "jarvis" or cont == 1:
                if cont == 0:
                 speak_text("Hello who will you like me to help you ") 
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                my_text = r.recognize_google(audio2)
                my_text = my_text.lower()
                messages.append ({'role':'user', 'content':my_text})
                response = send_to_chatGPT(messages)
                speak_text(response)
            elif my_text == "who are you":
                text = "I am Jarvis. Your personal assistant"
            elif my_text == "who am I":  
                text = "You are Zachary"
            elif my_text == "power down":
                text = "I do not understand your question."
            else: 
                text = "I do not understand your question."
            
            

            #Create a TTS object
            #tts = gTTS(text=text, lang='en')
            print(text)
            speak_text(text)
            #save converted speech to file
            #tts.save('C:\\Users\\jessi\\Documents\\matt_code\\output.mp3')
            #Play Sound
            #os.system("start C:\\Users\\jessi\\Documents\\matt_code\\output.mp3")

    except sr.RequestError as e:
        print("e")
    except sr.UnknownValueError :
        print("Listening.....")
    