from flask import session
from data.conexao import Conexao
import datetime

class Tarefas:
    def criar(titulo, descricao, prazo):
        try:
            if "usuario" not in session:
                raise Exception("Usuário não logado!")

            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor()

            sql = "INSERT INTO tbTarefas(titulo, descricao, prazo, usuario) VALUES(%s, %s, %s, %s)"
            valores = (titulo, descricao, prazo, session["usuario"])

            print("Dados que vão pro banco:", valores)  # DEBUG

            cursor.execute(sql, valores)
            conexao.commit()
            print("Tarefa criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar tarefa: {e}")
        finally:
            if 'conexao' in locals():
                conexao.close()

    def exibir():
        try: 
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor(dictionary=True)
            sql = "SELECT * FROM tbTarefas WHERE usuario = %s"
            valores = (session["usuario"],)  # <- vírgula aqui é essencial
            cursor.execute(sql, valores)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(f"Erro ao exibir tarefas: {e}")
        finally:
            if 'conexao' in locals():
                conexao.close()