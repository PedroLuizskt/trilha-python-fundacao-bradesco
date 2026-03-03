import datetime

class DataBase:
    """Camada de persistência de dados simulando um banco de dados relacional."""
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        """Carrega os dados físicos do disco para a memória (Dicionário)."""
        self.users = {}
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():
                        email, password, name, created = line.strip().split(";")
                        self.users[email] = (password, name, created)
        except FileNotFoundError:
            # Cria o arquivo caso seja a primeira execução
            open(self.filename, 'w').close()

    def get_user(self, email):
        """Retorna a tupla de dados do usuário ou -1 se não existir."""
        if email in self.users:
            return self.users[email]
        return -1

    def add_user(self, email, password, name):
        """Valida e insere um novo usuário na memória, seguido de flush no disco."""
        email = email.strip()
        if email not in self.users:
            self.users[email] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        return -1

    def validate(self, email, password):
        """Valida credenciais de acesso."""
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        return False

    def save(self):
        """Sincroniza o estado da memória com o disco (Flush)."""
        with open(self.filename, "w", encoding="utf-8") as file:
            for user in self.users:
                data = self.users[user]
                file.write(f"{user};{data[0]};{data[1]};{data[2]}\n")

    @staticmethod
    def get_date():
        """Gera o timestamp de criação."""
        return str(datetime.datetime.now()).split(" ")[0]