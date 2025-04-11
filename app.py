from flask import Flask, request, render_template, redirect, session
from model.controller_usuario import Usuario
from model.controller_tarefa import Tarefas
app = Flask(__name__)

app.secret_key = "aliciaamordaminhavida"
@app.route("/")
def pag_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro/usuario", methods=["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    Usuario.cadastro(usuario, nome, senha)
    return redirect("/login")

@app.route("/login")
def pag_login():
    return render_template("login.html")

@app.route("/login/usuario", methods=["POST"])
def login_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    esta_logado = Usuario.logar(usuario, senha)
    if esta_logado:
        return redirect("/pagInicial")
    else:
        return redirect("/")

@app.route("/pagInicial")
def pag_inicial():
    tarefa = Tarefas.exibir()
    return render_template("pag-inicial.html", tarefa = tarefa)

@app.route("/cadastro/tarefa", methods=["POST"])
def cadastrar_tarefa():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    prazo = request.form.get("prazo")
    Tarefas.criar(titulo, descricao, prazo)
    print(titulo)
    return redirect("/pagInicial")

app.run(debug=True)