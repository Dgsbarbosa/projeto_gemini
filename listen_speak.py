import speech_recognition as sr
from choice_voice import Voices_System
import pyttsx3
from choice_voice import Voices_System


class Speak:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.voices = Voices_System()
        self.voices_selected = self.voices.show_voices()
        
    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.pause_threshold = 0.5
            print("Ouvindo...")
            audio = self.recognizer.listen(source)
        try:
            texto = self.recognizer.recognize_google(audio, language='pt-br')
            return texto
        except sr.UnknownValueError:
            self.responder("Não entendi, pode repetir?")
            return self.ouvir_usuario()
        

    def speak(self, texto,language="" ):
        
        if language == "pt":
            self.engine.setProperty("voice",self.voices_selected["portuguese"].id)
        elif language == "en":
            self.engine.setProperty("voice",self.voices_selected["english"].id)
            
        self.engine.say(texto)
        self.engine.runAndWait()
        
        
