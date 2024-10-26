from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sentimiento_analizer import SentimientoAnalizer
from text_processor import TextProcessor
from translator_service import TranslatorService 


class SentimientoApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text='Ingrese un texto para revisar:')
        self.layout.add_widget(self.label)

        self.entrada_texto = TextInput(multiline=True, size_hint_y=None, height=200)
        self.layout.add_widget(self.entrada_texto)

        self.boton = Button(text='Analizar Sentimiento', size_hint_y=None, height=50)
        self.boton.bind(on_press=self.procesar_texto)
        self.layout.add_widget(self.boton)

        self.resultado = Label(text='', size_hint_y=None, height=50)
        self.layout.add_widget(self.resultado)

        return self.layout

    def procesar_texto(self, instance):
        texto = self.entrada_texto.text.strip()

        if texto:
            translator = TranslatorService()
            analyzer = SentimientoAnalizer()
            processor = TextProcessor(translator, analyzer) 

        sentimiento = processor.process(texto)
        self.resultado.text = f'Sentimiento: {sentimiento}'

if __name__ == '__main__':
    SentimientoApp().run()      