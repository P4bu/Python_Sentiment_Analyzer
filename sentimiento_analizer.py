from textblob import TextBlob

class SentimientoAnalizer:
    def analizar_sentimiento(self, texto_traducido: str) -> str:
        blob = TextBlob(texto_traducido)
        sentimiento = blob.sentiment.polarity
        #print('Polaridad: ', sentimiento)

        if sentimiento > 0:
            return 'Positivo'
        elif sentimiento < 0:
            return 'Negativo'
        else:
            return 'Neutral'