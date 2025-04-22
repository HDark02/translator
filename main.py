from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
import translate
from gtts.langs import _langs
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
        print(text)
        pass
MainApp().run()