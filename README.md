
# English Learning Assistant

## Descrição
Este projeto é um assistente de aprendizado de inglês que gera aulas interativas com base no nível de dificuldade e assunto escolhido pelo usuário. O assistente utiliza a API Gemini Pro da Google para gerar conteúdo de alta qualidade e a API Google Translate para tradução. O sistema também possui um sistema de reconhecimento de fala e síntese de voz para tornar a experiência de aprendizado mais envolvente.

## Funcionalidades
- **Geração de aulas**: gera aulas personalizadas com base no nível de dificuldade (fácil, médio, difícil) e assunto escolhido pelo usuário (aleatório ou definido pelo usuário).
- **Conteúdo da aula**: cada aula inclui um título, explicação em português e exemplos com frases em inglês e suas respectivas traduções em português.
- **Interação por voz**: o usuário pode ouvir as frases em inglês e praticar a pronúncia, com o sistema fornecendo feedback positivo.
- **Escolha de vozes**: o usuário pode escolher entre as vozes em inglês e português disponíveis no sistema.

## Tecnologias Utilizadas
- Python: linguagem de programação principal.
- Google Gemini Pro: modelo de linguagem de IA para geração de conteúdo.
- Google Translate: API para tradução de idiomas.
- SpeechRecognition: biblioteca para reconhecimento de fala.
- pyttsx3: biblioteca para síntese de voz.
- Colorama: biblioteca para colorir o texto no terminal.
- tqdm: biblioteca para criar barras de progresso.

## Instalação
Clone o repositório:
```bash
git clone git clone https://github.com/Dgsbarbosa/projeto_gemini.git

```
Crie um ambiente virtual:
```bash
python -m venv .venv
```
Ative o ambiente virtual:
```bash
source .venv/bin/activate
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
Configure a API key do Google Gemini Pro no arquivo .env.

## Utilização
Execute o script:
```bash
python script.py
```
Siga as instruções na tela para escolher o nível de dificuldade e assunto da aula.
Ouça as frases em inglês, pratique a pronúncia e receba feedback do sistema.

## Arquivos do Projeto
- script.py: arquivo principal do projeto que contém o fluxo principal do programa.
- listen_speak.py: contém as funções para reconhecimento e síntese de voz.
- generative_gemini.py: contém as funções para interação com a API Google Gemini Pro.
- choice_voice.py: contém as funções para seleção de vozes do sistema.

## Próximos Passos
- Implementar um sistema de avaliação para acompanhar o progresso do usuário.
- Adicionar mais recursos interativos, como jogos e quizzes.
- Expandir o banco de dados de exemplos e assuntos.
- Permitir que o usuário salve as aulas geradas.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request com suas sugestões de melhorias.

## Licença
Este projeto está licenciado sob a licença MIT.
```
Espero que isso ajude! Se você tiver mais perguntas ou precisar de mais assistência, sinta-se à vontade para perguntar.