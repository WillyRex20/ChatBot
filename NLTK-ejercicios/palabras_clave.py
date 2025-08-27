#Identificar las palabras clave mas relevantes en un texto
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

mensaje ="El procesamiento del lenguaje natural es una disciplina fascinante."
stop_word = set(stopwords.words("spanish"))
palabras = word_tokenize(mensaje)
palabras_clave = [word for word in palabras if word.lower() not in stop_word]

print("Palabras clave:", palabras_clave)