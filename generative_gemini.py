
import json
import pathlib
import sys
import textwrap
from time import sleep
import requests
import google.generativeai as genai
from dotenv import load_dotenv
import os
from IPython.display import display
from IPython.display import Markdown



class Generative:

    def __init__(self):
        self.config()

    def to_markdown(self, text):
        self.text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    def config(self):
        load_dotenv()
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

        genai.configure(api_key=self.GOOGLE_API_KEY)

        generation_config = {
            "candidate_count": 1,
            "temperature": 1,

        }

        self.model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                           generation_config=generation_config,



                                           )

    def chat(self, level, subject):


        format = {
            "aula": "",
            "nivel": "",
            "explicacao": "",
            "exemplos": [
                {
                    "pt": "",
                    "en": ""
                },
                {
                    "pt": "",
                    "en": ""
                },
                {
                    "pt": "",
                    "en": ""
                }
            ]
        }

        prompt = f"Como um professor especialista em ingles com doutorado em letras em harvard, crie uma aula de pratica de nivel {level} com o assunto {subject}, o formato deve ser {format} adicione mais exemplos, retorne em json a aula sera narrada, o nome da aula, a explicação deve ser em portugues, não mude os nomes das chaves do formato e retire as aspas antes e depois do json"

        try:
            
            print("Gerando aula...")
            response = self.model.generate_content(prompt)           
            
             # Carrega a resposta como um objeto Python
            response_obj = json.loads(response.text)

    # Serializa o objeto Python de volta para uma string JSON
            response_text = json.dumps(response_obj, ensure_ascii=False)

            # print(response_text)
            self.to_markdown(response_text)

        except NameError:
            print(f"Ocorreu um erro {NameError}, escolha novamente\n")
            print("Encerrando o programa....")
            sleep(1)
            sys.exit()

        return response_obj
        

# run = Generative()
# run.chat("1","1")

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
