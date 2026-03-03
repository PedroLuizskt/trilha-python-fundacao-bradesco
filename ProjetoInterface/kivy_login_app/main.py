from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

# Inicialização da Camada de Dados Global
db = DataBase("users.txt")

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        # Validação de regras de negócio básicas
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                # Comunicação com o BD
                status = db.add_user(self.email.text, self.password.text, self.namee.text)
                if status == 1:
                    self.reset()
                    self.manager.current = "login"
                else:
                    invalidForm("Email já cadastrado.")
            else:
                invalidForm("A senha não pode estar em branco.")
        else:
            invalidForm("Preencha os dados corretamente (Email válido).")

    def login(self):
        self.reset()
        self.manager.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            # Envia o e-mail logado para a MainWindow processar
            MainWindow.current_user = self.email.text
            self.reset()
            self.manager.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        self.manager.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current_user = ""

    def logOut(self):
        self.manager.current = "login"

    def on_enter(self, *args):
        # Método mágico do Kivy acionado ao entrar na tela
        password, name, created = db.get_user(MainWindow.current_user)
        self.n.text = "Nome da Conta: " + name
        self.email.text = "Email: " + MainWindow.current_user
        self.created.text = "Criado em: " + created


class WindowManager(ScreenManager):
    pass

# Tratamento de Exceções Visuais (Popups)
def invalidLogin():
    pop = Popup(title='Falha no Login',
                content=Label(text='Email ou Senha inválidos.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm(msg='Por favor, preencha todos os campos corretamente.'):
    pop = Popup(title='Formulário Inválido',
                content=Label(text=msg),
                size_hint=(None, None), size=(400, 400))
    pop.open()

# Carregamento da View e Definição das Rotas
kv = Builder.load_file("my.kv")

sm = WindowManager()
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()