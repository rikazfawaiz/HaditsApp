from kivymd.app import MDApp
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.core.text.markup import MarkupLabel
from kivy.config import Config



class MyApp(MDApp):

    def build(self):

        # Register the Arabic font
        LabelBase.register(name='Arabic', fn_regular='font/mcs-book-title-5.TTF')

        # Set the default font for KivyMD
        Config.set('kivy', 'default_font', 'Arabic')

        return MarkupLabel(text='حَدَّثَنَا عَبْدُ اللَّهِ بْنُ مَسْلَمَةَ بْنِ قَعْنَبٍ', font_size=20)



if __name__ == '__main__':
    MyApp().run()

