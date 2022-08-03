from pytesseract import pytesseract
from translate import Translator
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

Window.size = (900, 600)
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract

image = ObjectProperty(None)
translation = ObjectProperty(None)
recognised_text = ObjectProperty(None)


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    def ocr(self):
        global image, recognised_text
        if type(recognised_text) == str:
            self.ids.text_output.text = recognised_text
            return
        try:
            recognised_text = pytesseract.image_to_string(image, config='--psm 6')
            self.ids.text_output.text = recognised_text
        except:
            self.ids.text_output.text = 'Please, select the source image'

    def translate_to_bg(self):
        global translation
        if type(translation) == str:
            self.ids.text_output.text = translation
            return
        translation = ''
        translator = Translator(from_lang="en", to_lang="bg")
        try:
            for sentence in recognised_text.split('\n'):
                translation += f'{translator.translate(sentence)}\n'
            self.ids.text_output.text = translation
        except:
            self.ids.text_output.text = 'There is no text to translate'

    def reset(self):
        global image, translation, recognised_text
        image = None
        translation = None
        translation = None
        recognised_text = None
        self.ids.text_output.text = ''


class FileChooserWindow(Screen):
    image_name = ObjectProperty(None)

    def selected(self, filename):
        global image
        self.ids.text_image.source = filename[0]
        image = filename[0]
        return image


kv = Builder.load_file('ui.kv')


class TextRecognition(App):
    def build(self):
        return kv


if __name__ == '__main__':
    TextRecognition().run()
