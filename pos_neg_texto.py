#Determinar si un texto tiene connotacion positiva o negativa

from nltk.sentiment import SentimentIntensityAnalyzer
mensaje = "Exitos amigo"
sia = SentimentIntensityAnalyzer()
resultado = sia.polarity_scores(mensaje)
print("Analisis de sentimiento:", resultado)


  