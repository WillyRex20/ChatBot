#Asignar una etiqueta a cada palabra
from nltk import pos_tag
from nltk.tokenize import word_tokenize

mensaje = "NLTK es unas libreria increible para el PLN"
palabras = word_tokenize(mensaje)
etiquetas = pos_tag(palabras)
print(etiquetas)