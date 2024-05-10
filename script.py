from listen_speak import Speak
from time import sleep

from googletrans import Translator

speaks = Speak()






speaks.speak("pt","Olá você conseguiu")

sleep(1)

speaks.speak("en","Hello, you got it")

def detect_language(text):
    translator = Translator()
    language = translator.detect(text)

    print(language.lang)
    return language.lang

text = detect_language("minha casa")





# while True:
    
#     texto_usuario = classe.ouvir_usuario()
#     texto_padrao = "ola amigo"
    
#     print(texto_usuario)
    
#     if texto_usuario:  # Só responde se ouvir algo
#         print(f"Você disse: {texto_usuario}")
#         classe.responder("Recebi sua mensagem!")
        
#     sleep(0.5)