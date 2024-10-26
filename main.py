from textblob import TextBlob
from googletrans import Translator


class TranslatorService:
    def traduccion_texto(self, texto: str) -> str:
        traduccion = Translator()
        #print(texto_traducido)
        return traduccion.translate(texto, src='es', dest='en').text


class SentimientoAnalizer:
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

class Processor:
    def __init__(self, translator:TranslatorService, analyzer:SentimientoAnalizer):
        self.translator = translator
        self.analyzer = analyzer

    def process(self, texto: str) -> str:
        texto_traducido = self.translator.translate(texto)
        sentimiento = self.analyzer.analyzer(texto_traducido)
        return sentimiento    

def run():
    texto = input('Ingrese un texto para revisar: ')
    Translator = TranslatorService()
    analyzer = SentimientoAnalizer()
    processor = Processor() 

    sentimiento = processor.process(texto)
    print(f'Sentimiento ->  {sentimiento}' )

if __name__ == '__main__':
    run()      