from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file("QuizPage.kv")
class QuizPageApp(App):
    def build(self):
        return QuizManager()


class QuizManager(ScreenManager):
    pass


class Question1Screen(Screen):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"


class Question2Screen(Screen):
    pass


class CorrectScreen(Screen):
    pass


class IncorrectScreen(Screen):
    pass


QuizPageApp().run()
