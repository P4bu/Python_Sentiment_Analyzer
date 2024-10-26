from googletrans import Translator


class TranslatorService:
    def traduccion_texto(self, texto: str) -> str:
        traduccion = Translator()
        #print(texto_traducido)
        return traduccion.translate(texto, src='es', dest='en').text

