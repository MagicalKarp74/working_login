import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("login_page.kv")

accounts = {"A" : "Aa1!", "Evil Mc Eviler" : "2Evil >:)"}

nums = "1234567890"
specials = "~`!@#$%^&*()_+=,<.>/?;:[{]}}\|]"
#sdfs
class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass

class LoginScreen(Screen,BoxLayout):

    def check_login(self,name,passwrd):
        if name in accounts:
            if accounts[name] == passwrd:
                self.manager.current = "Logged"
        else:
            self.ids.bobby.text = "This account does not exist"

    def move_screen(self):
        self.manager.current = "reg"

class RegisterScreen(Screen,BoxLayout):

    #I know this looks really bad

    def check_registration(self,name,passwrd,passwrd2):
        number=0
        if name not in accounts:
            if passwrd.lower() != passwrd and passwrd.upper() != passwrd:
                for num in nums:
                    if num in passwrd:
                        number+=1
                if number > 0:
                    number = 0
                    for special in specials:
                        if special in passwrd:
                            number+=1
                    if number > 0:
                            if passwrd == passwrd2:
                                accounts[name] = passwrd
                                self.manager.current = "Log"
                            else:
                                self.ids.bob.text = "Reentered password does not match"
                    else:
                        self.ids.bob.text = "Password needs a special character"
                else:
                    self.ids.bob.text = "Password needs a number"

            else:
                self.ids.bob.text = "Password Needs a upper and lowercase"
        else:
            self.ids.bob.text = "This username is taken"





class LoggedInScreen(Screen,BoxLayout):
    def log_out(self):
        self.manager.current = "Log"

LoginPageApp().run()