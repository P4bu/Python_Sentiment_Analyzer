from sentimiento_analizer import SentimientoAnalizer
from text_processor import TextProcessor
from translator_service import TranslatorService 


def run():
    texto = input('Ingrese un texto para revisar: ')
    translator = TranslatorService()
    analyzer = SentimientoAnalizer()
    processor = TextProcessor(translator, analyzer) 

    sentimiento = processor.process(texto)
    print(f'Sentimiento ->  {sentimiento}' )

if __name__ == '__main__':
    run()      