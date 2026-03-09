import sqlite3

class Database:
    def __init__(self, db_name="clientes.db"):
        self.db_name = db_name
        self._criar_tabela()

    # Método privado arquitetural: gerencia conexões e cursores com segurança
    def _execute_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            conn.commit()
            return cursor.fetchall()

    def _criar_tabela(self):
        query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            email TEXT,
            cpf TEXT
        )
        """
        self._execute_query(query)

    def insert(self, nome, sobrenome, email, cpf):
        query = "INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (?, ?, ?, ?)"
        self._execute_query(query, (nome, sobrenome, email, cpf))

    def view(self):
        query = "SELECT * FROM clientes"
        return self._execute_query(query)

    def search(self, nome="", sobrenome="", email="", cpf=""):
        query = "SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?"
        return self._execute_query(query, (nome, sobrenome, email, cpf))

    def delete(self, id):
        query = "DELETE FROM clientes WHERE id=?"
        self._execute_query(query, (id,))

    def update(self, id, nome, sobrenome, email, cpf):
        query = "UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?"
        self._execute_query(query, (nome, sobrenome, email, cpf, id))