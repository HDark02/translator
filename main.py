from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
import translate
import os
import platform
from kivy.core.clipboard import Clipboard
from kivymd.toast.kivytoast.kivytoast import toast
# Vérifier si le système est Windowse
if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
_langs={'af': 'Afrikaans', 'am': 'Amharic', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'eu': 'Basque', 'fi': 'Finnish', 'fr': 'French', 'fr-CA': 'French (Canada)', 'gl': 'Galician', 'gu': 'Gujarati', 'ha': 'Hausa', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iw': 'Hebrew', 'ja': 'Japanese', 'jw': 'Javanese', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin', 'lt': 'Lithuanian', 'lv': 'Latvian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ms': 'Malay', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi (Gurmukhi)', 'pl': 'Polish', 'pt': 'Portuguese (Brazil)', 'pt-PT': 'Portuguese (Portugal)', 'ro': 'Romanian', 'ru': 'Russian', 'si': 'Sinhala', 'sk': 'Slovak', 'sq': 'Albanian', 'sr': 'Serbian', 'su': 'Sundanese', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'yue': 'Cantonese', 'zh-CN': 'Chinese (Simplified)', 'zh-TW': 'Chinese (Traditional)'}
class MainApp(MDApp) :
    def on_start(self):
        global values, values_lang
        values=[]
        values_lang=[]
        for x, y in _langs.items():
            values.append(x)
            values_lang.append(y)
        Home.ids.lang_in.lang_list_id.values = values_lang
        Home.ids.lang_out.lang_list_id.values = values_lang
    def build(self) :
        global Home
        Home = Builder.load_file("interface.kv")
        return Home
    def looking(self, lang):
        i = values_lang.index(lang)
        lang = values[i]
        return lang
    def translate(self, text, lang_in, lang_out):
        lang_in=self.looking(lang_in)
        lang_out=self.looking(lang_out)
        try:
            translation = translate.Translator(from_lang=lang_in, to_lang=lang_out)
            result = translation.translate(text)
        except:
            result = ""
        Home.ids.output.text_enter.text = result
    def copy_text(self, text):
        Clipboard.copy(text)

        # Afficher un message de confirmation dans la console
        toast("Texte copié !")

if __name__== "__main__":
    MainApp().run()

