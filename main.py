from textblob import TextBlob
from googletrans import Translator


class TranslatorService:
    def traduccion_texto(self, texto: str) -> str:
        traduccion = Translator()
        #print(texto_traducido)
        return traduccion.translate(texto, src='es', dest='en').text


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

class TextProcessor:
    def __init__(self, translator:TranslatorService, analyzer:SentimientoAnalizer):
        self.translator = translator
        self.analyzer = analyzer

    def process(self, texto: str) -> str:
        texto_traducido = self.translator.traduccion_texto(texto)
        sentimiento = self.analyzer.analizar_sentimiento(texto_traducido)
        return sentimiento    

def run():
    texto = input('Ingrese un texto para revisar: ')
    translator = TranslatorService()
    analyzer = SentimientoAnalizer()
    processor = TextProcessor(translator, analyzer) 

    sentimiento = processor.process(texto)
    print(f'Sentimiento ->  {sentimiento}' )

if __name__ == '__main__':
    run()      