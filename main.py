from search import search_hadith
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.metrics import dp
from kivy.core.text import LabelBase


class MyApp(MDApp):

    result_hadits = []

    def build(self):
        self.title = "AppHadits"

        # Main layout
        self.main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=2)

        # Attribute 1: Title Label
        title_label = MDLabel(text="Cari Hadits", halign="center", font_style="H4", size_hint_y=None, height=dp(50))
        self.main_layout.add_widget(title_label)

        # Attribute 2: Text Input
        self.input_text = MDTextField(hint_text="Enter your sentence", multiline=True)
        self.main_layout.add_widget(self.input_text)

        # Attribute 3: Search Button
        search_button = MDRaisedButton(text="Search", on_release=self.on_search)
        self.main_layout.add_widget(search_button)

        # Attribute 4: Result
        self.sv = ScrollView()
        self.ml = MDList()
        self.sv.add_widget(self.ml)
        self.update_result_view()  # Initialize the ScrollView with the initial results
        self.main_layout.add_widget(self.sv)

        return self.main_layout

    def update_result_view(self):
        # Clear existing content
        self.ml.clear_widgets()
        # Populate ScrollView with search results
        for hadits in self.result_hadits:
            print(hadits)
            hadits = f"similarity_score : {hadits['similarity_score']}\nsource: {hadits['file'].split('/')[-1].split('.')[0]}\n{hadits['hadith']['arab']}\n{hadits['hadith']['id']}"
            # hadits = hadits['hadith']['arab']
            self.ml.add_widget(
                MDTextField(
                    text=hadits, 
                    multiline=True,
                    readonly=True,
                    halign="left",
                    font_size=14
                ) 
            )

    def on_search(self, instance):
        self.result_hadits = search_hadith(self.input_text.text)
        self.update_result_view()  # Update the ScrollView with the new search results


if __name__ == '__main__':
    MyApp().run()
