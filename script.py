import sys
from listen_speak import Speak
from time import sleep
from generative_gemini import Generative
from googletrans import Translator
from tqdm import tqdm
from colorama import Fore, init


speaks = Speak()

def choices():
    
    level_english = {
        "1":"fácil",
        "2": "médio",
        "3": "Dificil"
        
    }

    subject = {
        "1":"Aleatório",
        "2": "Escolher o assunto"
    }
    
    while True:
        print()
        for item in level_english:
            print(f"{item} - {level_english[item]}",end="  ")
            
        choice_level = input("\n\nQual o nivel de dificuldade? ")
        
        if choice_level in level_english:
            print(f"")
            choice_level = level_english[choice_level]
            break
        else:
            print("\nDigite uma valor válido")
            
    while True:
        print()
        for item in subject:
            print(f"{item} - {subject[item]}",end="  ")
            
        choice_subject = input("\n\nQual o assunto? ")
        
        if choice_subject in subject:
            if choice_subject == "2":
                text_subject = input("Digite o assunto? ")
                choice_subject= text_subject
            break
        else:
            print("\nDigite uma valor válido")
            
        

    return choice_level, choice_subject


def detect_language(text):
    translator = Translator()
    language = translator.translate(text)

    
    return language.text




print("\nBem vindo ao assistente de aprendizado de ingles...\n")              
for i in tqdm(range(100)):
    sleep(0.05)
    
level, subject = choices()

generative = Generative()

response =  generative.chat(level, subject)


class_name = response["aula"]
explanation = response["explicacao"]
examples = response["exemplos"]

print(f"\nNome da aula: \n{class_name}\n")

print(f"Descrição:\n{explanation}\n")


while True:
    go_examples = input("Gostaria de iniciar os exemplos? s (sim) ou n(não):  ").lower()
    
    if go_examples == "s":
        speaks.speak("Vamos iniciar nossos exemplos", "pt")
        break
    
    elif go_examples =="n":
        print("Encerrando o programa...")
        sleep(1)
        sys.exit()

    else:
        continue

def speak_example(dict):
    
    phrase_pt = dict["pt"]
    phrase_en = dict["en"]
    
    
    speaks.speak(phrase_pt, "pt")
    
    print(f"Origin: {phrase_en}")
    print(f"\nTradução: {phrase_pt}")
    
    
    for _ in range(3):
        
        speaks.speak(phrase_en, "en")
        sleep(1)
        speaks.speak("Repeat", "en")
        sleep(3)
    
    speaks.speak("Great","en")    
    
    sleep(1)
    
for example in examples:
    
    speak_example(example)

