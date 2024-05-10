import pyttsx3
import sys


class Voices_System:
    
    def __init__(self) :
        self.engine = pyttsx3.init()
        # self.engine.setProperty('rate', 160)  # Set the speaking rate
        self.engine.setProperty('volume', 1.0)
        self.voices = self.engine.getProperty('voices')
        self.search_voices()
        
        print("Buscando vozes no sistema...")
        
        
     
    # procura as vozes do sistema 
    def search_voices(self):
        
        self.english_voices = []
        self.portuguese_voices = []

        # seleciona as vozes em ingles disponiveis no sistema
        for voice in self.voices:
            
            if "EN-US" in voice.id:
                
                self.english_voices.append(voice)
            
            elif "PT-BR" in voice.id:
                self.portuguese_voices.append(voice)
            
        return self.english_voices, self.portuguese_voices

    
    def show_voices(self):
        
        english_voices, portuguese_voices = self.search_voices()
        
        portuguese_voice = None
        english_voice = None
        
        print("\nVozes disponiveis em Português:\n")             
   
        for i, voice in enumerate(portuguese_voices):
            
            self.voice_index = i + 1
            self.voice_id = voice.id
            self.voice_name = voice.name
            self.voice_name = self.voice_name.split(" ")
            self.voice_name = self.voice_name[1]
            self.text_voice = f"Olá meu nome é {self.voice_name}, "
            
            if len(portuguese_voices) == 1:
                 self.text_voice = self.text_voice +  "Eu sou a única voz em Português no seu sistema , o que você achou de mim?"
                 portuguese_voice = portuguese_voices[0]
                 
            elif len(portuguese_voices) > 1:
                self.text_voice = self.text_voice + f"Eu sou a voz em Português número {self.voice_index}" 
                
            else:
                print("Não foi encontrada uma voz em português.")
                
                print("Encerrando o programa")
                sys.exit()
            
            
            self.engine.setProperty('voice', self.voice_id)
            
         
           
            self.engine.say(self.text_voice)
            
            self.engine.runAndWait()   
                     
        for i, voice in enumerate(portuguese_voices):
            print(f"{i+1} - {voice.name}")   
                  
        while True:
            
            if len(portuguese_voices) <= 1:
                break
                    
                
            choice_portuguese = input("Escolha: ")
            
            if int(choice_portuguese) > len(portuguese_voices) or int(choice_portuguese) == "" or choice_portuguese.isdigit() == False:
                continue
                
            else:
                
                portuguese_voice = portuguese_voices[int(choice_portuguese)-1]
                break
        
        
        print("\nVozes disponiveis em ingles:\n")     
            
        for i, voice in enumerate(english_voices):
            
            self.voice_index = i + 1
            self.voice_id = voice.id
            self.voice_name = voice.name
            self.voice_name = self.voice_name.split(" ")
            self.voice_name = self.voice_name[1]
            self.text_voice = f"Hello, my name is {self.voice_name}, "
            
            if len(english_voices) == 1:
                
                 self.text_voice = self.text_voice +  'I am the only English voice in your system, what did you think of me?'
                 
                 print(f"Tradução: Olá eu sou o {self.voice_name},  Eu sou a única voz em Inglês no seu sistema , o que você achou de mim?\n")
                 english_voice = portuguese_voices[0]
                 
            elif len(english_voices) > 1:
                self.text_voice = self.text_voice + f'I am the English voice number {self.voice_index}'
                print(f'Tradução: "Olá eu sou o {self.voice_name} Eu sou a voz em Inglês número" {self.voice_index}') 
                
                
            else:
                print("A English voice was not found.")
                print("Closing the program")
                sys.exit()
            
            
            self.engine.setProperty('voice', self.voice_id)
            
            
         
           
            self.engine.say(self.text_voice)
            
            self.engine.runAndWait()   
            
        print()            
        
        for i, voice in enumerate(english_voices):
            print(f"{i+1} - {voice.name}")         
                
        while True:
            
            if len(english_voices) <= 1:
                break
            
            
                
            choice_english = input("\nEscolha: \n")
            
            if int(choice_english) > len(english_voices)  or int(choice_english) == "" or choice_english.isdigit() == False:
                continue
                
            else:
                
                english_voice = english_voices[int(choice_english)-1]
                break
            
     
        return {"portuguese": portuguese_voice, "english": english_voice}
        
        
 



