import kivy

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class PDF_Master_App(App):
    def build(self):

        return Label(text ="Hello Geeks")

pdfMaster = PDF_Master_App()
pdfMaster.run()