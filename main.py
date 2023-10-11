from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

users={}
Builder.load_file("LoginPage.kv")

class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass


class Query(Screen):
    def answer_question(self,unam,pwrd):
        if unam in users:
            if users[unam]==pwrd:
                self.manager.current = "cor"
        else:
            self.ids.test.text = "Incorrect Username Or Password"
    def advance(self):
        self.manager.current = "add"


class Creation(Screen):
    def answer_question(self,unam,pwrd,cfrm):
        self.ids.test.text = ""
        a=True
        if unam in users:
            a=False
            self.ids.test.text += "Username Taken\n"
        b = True
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i in pwrd:
                b = False
        if b:
            a = False
            self.ids.test.text += "Capital Required\n"
        b = True
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in pwrd:
                b = False
        if b:
            a = False
            self.ids.test.text += "Lowercase Required\n"
        b = True
        for i in range(10):
            if str(i) in pwrd:
                b = False
        if b:
            a = False
            self.ids.test.text += "Number Required\n"

        b = True
        for i in pwrd:
            if i in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890":
                b = False
        if b:
            a = False
            self.ids.test.text += "Special Character Required\n"
        if len(pwrd) < 8:
            a = False
            self.ids.test.text += "At Least 8 Characters Required\n"
        if cfrm != pwrd:
            a = False
            self.ids.test.text += "Password Does Not Match Confirmation"
        if a:
            users[unam] = pwrd
            self.manager.current = "que"






class Interior(Screen):
    def advance(self):
        self.manager.current = "que"

LoginPageApp().run()
