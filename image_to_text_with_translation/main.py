from PIL import Image
from pytesseract import pytesseract
from translate import Translator
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (600, 600)
assert isinstance(Window, object)
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def ocr():
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(r'D:\d.png')
    output = pytesseract.image_to_string(img)
    with open(r'D:\converted.txt', 'w') as f:
        f.write(output)
    return output


def translate_to_bg():
    with open(r'D:\converted.txt', 'w') as f:
        f.write(text)

    translation = ''
    translator = Translator(from_lang="en", to_lang="bg")
    for sentence in text.split('\n'):
        translation += f'{translator.translate(sentence)}\n'

    with open(r'D:\translated.txt', 'w') as f:
        f.write(translation)
    return translation


text = ocr()
# print(text)


class MainWidget(Widget):
    ocr_text = text
    input_path_text = 'Enter the path to save text files HERE:'

    def translate_press(self):
        output_text = translate_to_bg()
        self.ids.translated_box.text = output_text
        self.ids.translate_button.text = 'TRANSLATED TEXT SAVED'
        self.ids.copy_button.text = 'COPY TO CLIPBOARD'

    def copy_button_on_release(self):
        self.ids.copy_button.text = 'COPIED TO CLIPBOARD'


class ImageToText(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    ImageToText().run()
