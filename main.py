from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
Builder.load_file('frontend.kv')
import requests


class FirstScreen(Screen):
    def search_image(self):
        #get text from user
        query =self.manager.current_screen.ids.user_query.text
        #open respective wikipedia page
        page = wikipedia.page(query)
        #get the first image from wiki
        link = page.images[0]
        #download the image
        req = requests.get(link)
        imagepath = f'files/{query}.jpeg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        #set the image in the image widget
        self.manager.current_screen.ids.img.source= imagepath


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
