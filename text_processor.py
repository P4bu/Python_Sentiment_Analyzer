from translator_service import TranslatorService
from sentimiento_analizer import SentimientoAnalizer

class TextProcessor:
    def __init__(self, translator:TranslatorService, analyzer:SentimientoAnalizer):
        self.translator = translator
        self.analyzer = analyzer

    def process(self, texto: str) -> str:
        texto_traducido = self.translator.traduccion_texto(texto)
        sentimiento = self.analyzer.analizar_sentimiento(texto_traducido)
        print(texto_traducido)
        return sentimiento   