#vamos a importar un texto en palabras o frases
import nltk
nltk.download('all')

from nltk.tokenize import word_tokenize, sent_tokenize

mensaje = "Hola ¿Como estas? Bienvenido al mundo NLTK un gran poder conlleva una gran responsabilidad"

palabras = word_tokenize(mensaje)
oraciones = sent_tokenize(mensaje)

print("palabras: ", palabras)
print("oraciones", oraciones)

