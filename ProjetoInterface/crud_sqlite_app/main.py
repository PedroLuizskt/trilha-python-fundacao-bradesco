import tkinter as tk
from tkinter import messagebox
from database import Database

class AppCliente:
    def __init__(self, root):
        self.db = Database() # Instancia a conexão segura com o banco
        self.root = root
        self.root.title("Sistema Profissional de Cadastro de Clientes")
        self.root.geometry("600x400")
        
        # Variável de classe para substituir a perigosa "global selected"
        self.selected_tuple = None 

        self._build_gui()
        self.view_command() # Carrega os dados ao abrir

    def _build_gui(self):
        # --- Variáveis de Entrada ---
        self.txtNome = tk.StringVar()
        self.txtSobrenome = tk.StringVar()
        self.txtEmail = tk.StringVar()
        self.txtCPF = tk.StringVar()

        # --- Labels e Entries (Usando Grid) ---
        tk.Label(self.root, text="Nome:").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        tk.Entry(self.root, textvariable=self.txtNome, width=25).grid(row=0, column=1)

        tk.Label(self.root, text="Sobrenome:").grid(row=0, column=2, pady=5, padx=5, sticky="e")
        tk.Entry(self.root, textvariable=self.txtSobrenome, width=25).grid(row=0, column=3)

        tk.Label(self.root, text="E-mail:").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        tk.Entry(self.root, textvariable=self.txtEmail, width=25).grid(row=1, column=1)

        tk.Label(self.root, text="CPF:").grid(row=1, column=2, pady=5, padx=5, sticky="e")
        tk.Entry(self.root, textvariable=self.txtCPF, width=25).grid(row=1, column=3)

        # --- ListBox e Scrollbar ---
        self.listClientes = tk.Listbox(self.root, height=10, width=60)
        self.listClientes.grid(row=2, column=0, rowspan=6, columnspan=2, pady=10, padx=10)
        
        sb = tk.Scrollbar(self.root)
        sb.grid(row=2, column=2, rowspan=6, sticky="ns", pady=10)
        
        self.listClientes.configure(yscrollcommand=sb.set)
        sb.configure(command=self.listClientes.yview)

        # BIND: O evento de clique na lista chama a função de forma segura
        self.listClientes.bind('<<ListboxSelect>>', self.get_selected_row)

        # --- Botões ---
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=2, column=3, rowspan=6, sticky="n", pady=10)

        tk.Button(btn_frame, text="Ver Todos", width=15, command=self.view_command).pack(pady=2)
        tk.Button(btn_frame, text="Buscar", width=15, command=self.search_command).pack(pady=2)
        tk.Button(btn_frame, text="Inserir", width=15, command=self.insert_command).pack(pady=2)
        tk.Button(btn_frame, text="Atualizar", width=15, command=self.update_command).pack(pady=2)
        tk.Button(btn_frame, text="Deletar", width=15, command=self.delete_command).pack(pady=2)
        tk.Button(btn_frame, text="Limpar Campos", width=15, command=self.clear_entries).pack(pady=2)

    # --- Funções Lógicas (Controllers) ---
    def clear_entries(self):
        self.txtNome.set("")
        self.txtSobrenome.set("")
        self.txtEmail.set("")
        self.txtCPF.set("")

    def get_selected_row(self, event):
        try:
            index = self.listClientes.curselection()[0]
            self.selected_tuple = self.listClientes.get(index)
            self.clear_entries()
            # Preenche os campos com os dados selecionados (ignorando o ID na pos 0)
            self.txtNome.set(self.selected_tuple[1])
            self.txtSobrenome.set(self.selected_tuple[2])
            self.txtEmail.set(self.selected_tuple[3])
            self.txtCPF.set(self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.listClientes.delete(0, tk.END)
        for row in self.db.view():
            self.listClientes.insert(tk.END, row)

    def search_command(self):
        self.listClientes.delete(0, tk.END)
        for row in self.db.search(self.txtNome.get(), self.txtSobrenome.get(), self.txtEmail.get(), self.txtCPF.get()):
            self.listClientes.insert(tk.END, row)

    def insert_command(self):
        if self.txtNome.get() == "":
            messagebox.showwarning("Aviso", "O nome não pode estar vazio!")
            return
        self.db.insert(self.txtNome.get(), self.txtSobrenome.get(), self.txtEmail.get(), self.txtCPF.get())
        self.view_command()
        self.clear_entries()

    def update_command(self):
        if self.selected_tuple:
            self.db.update(self.selected_tuple[0], self.txtNome.get(), self.txtSobrenome.get(), self.txtEmail.get(), self.txtCPF.get())
            self.view_command()

    def delete_command(self):
        if self.selected_tuple:
            self.db.delete(self.selected_tuple[0])
            self.clear_entries()
            self.view_command()

# --- Ponto de Execução ---
if __name__ == "__main__":
    janela = tk.Tk()
    aplicacao = AppCliente(janela)
    janela.mainloop()