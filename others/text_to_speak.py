import pyttsx3 # importamos o modúlo

en = pyttsx3.init() # meotodo init seleciona um ending de sintetização, no caso o espeak
en.say("Hello, I am Ronan") # o metodo say para dizer o que queremos
en.say("Nice to meet you")
en.runAndWait() # para ouvir o que foi escrito
voices = en.getProperty('voices')
print()
en.setProperty('voice', voices[2].id) # mudamos a propriedade setando pelo id para pt-br, o lemento b diz que a string está em bytes
en.say('Olá, tudo bem?')
en.runAndWait()