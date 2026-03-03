# 🔐 App de Autenticação com Kivy (Projeto 1)

![Interface do Aplicativo](docs/example.png)

## 📌 Sobre o Projeto
Desenvolvi este sistema completo de login e registro de usuários como o primeiro projeto prático da Trilha de Python da Fundação Bradesco. A aplicação simula um fluxo real de autenticação, possuindo validação de credenciais, persistência local de dados e transição dinâmica de telas.

## 🛠️ Ferramentas e Tecnologias
* **Python 3.x:** Linguagem principal do ecossistema.
* **Kivy:** Framework multiplataforma utilizado para a renderização da Interface Gráfica (GUI) com aceleração via OpenGL.
* **Padrão MVC (Model-View-Controller):** Arquitetura adotada para separar a interface visual da lógica de negócios.

## 🚀 Melhorias e Arquitetura Implementada
Para elevar o nível do projeto original proposto no curso para um padrão de mercado, apliquei diversos conceitos de Engenharia de Software e refatorei a base de código:

* **Separação de Responsabilidades (SoC):** Isolei a marcação do layout no arquivo declarativo `my.kv` (View), mantendo o `main.py` (Controller) limpo e focado puramente na lógica de roteamento (`ScreenManager`).
* **I/O Seguro (Context Managers):** Refatorei o módulo `database.py` (Model) substituindo a abertura clássica de arquivos pela estrutura `with open(...)`. Isso garante a liberação correta dos *File Descriptors* do Sistema Operacional e previne corrupção de dados.
* **Orientação a Objetos Avançada:** Utilizei classes abstratas do Kivy (`Screen`) para modularizar cada tela e centralizei o gerenciamento do estado dos usuários.
* **Tratamento de Exceções Visual:** Implementei `Popups` nativos para alertar o usuário sobre credenciais inválidas ou formulários vazios, garantindo uma UX (User Experience) resiliente.

## ⚙️ Como Executar Localmente

Siga os passos abaixo para rodar a aplicação em sua máquina:

1. **Clone o repositório e navegue até a pasta do projeto:**
   ```bash
   cd kivy_login_app

2. **Crie e ative um Ambiente Virtual (Venv):**
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

```


3. **Instale as dependências do Kivy:**
```bash
python -m pip install --upgrade pip setuptools virtualenv
pip install kivy[base] kivy_deps.sdl2 kivy_deps.glew

```


4. **Execute o aplicativo:**
```bash
python main.py

```



## 📁 Estrutura de Arquivos

```text
kivy_login_app/
│
├── database.py       # Lógica de manipulação do banco de dados (.txt)
├── main.py           # Ponto de entrada, lógica de telas e popups
├── my.kv             # Estrutura declarativa da Interface Gráfica
├── users.txt         # Arquivo gerado automaticamente contendo os dados
└── docs/
    └── example.png   # Screenshot da interface

```

