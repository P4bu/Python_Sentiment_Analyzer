from textblob import TextBlob
from googletrans import Translator


def traduccion_texto(texto):
    traduccion = Translator()
    texto_traducido = traduccion.translate(texto, src='es', dest='en').text
    #print(texto_traducido)
    return texto_traducido


def analizar_sentimiento(texto_traducido):

    blob = TextBlob(texto_traducido)
    
    sentimiento = blob.sentiment.polarity
    #print('Polaridad: ', sentimiento)

    if sentimiento > 0:
        return 'Positivo'
    elif sentimiento < 0:
        return 'Negativo'
    else:
        return 'Neutral'

def run():
    texto = input('Ingrese un texto para revisar: ')
    texto_traducido = traduccion_texto(texto)
    sentimiento = analizar_sentimiento(texto_traducido)

    print(f'Sentimiento ->  {sentimiento}' )

if __name__ == '__main__':
    run()      