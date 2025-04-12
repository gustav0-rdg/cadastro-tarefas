from data.conexao import Conexao
from hashlib import sha256
from flask import session
import mysql.connector
import traceback

class Usuario:
    # Função para cadastrar Usuario
    def cadastro(usuario, nome, senha):
        senha = sha256(str(senha).encode()).hexdigest()
        try:
            # Criando conexao
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor() 
            # Codigo SQL
            sql = "INSERT INTO tbUser(usuario, nome, senha_usuario) VALUES(%s, %s, %s);"
            valores = (usuario, nome, senha)
            cursor.execute(sql, valores)
            # Concluido a insersão
            conexao.commit()
        except Exception as e:
            print(f"Falha ao inserir usuario: {e}")
        finally:
            if 'conexao' in locals():
                conexao.close()
    
    # Funcao de Login no usuario
    def logar(usuario, senha):
        senha = sha256(str(senha).encode()).hexdigest()
        try:
            conexao = Conexao.criar_conexao()
            cursor = conexao.cursor(dictionary=True)
            sql = "SELECT * FROM tbUser WHERE usuario = %s and BINARY senha_usuario = %s;"
            valores = (usuario, senha)
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()
            # Caso resultado retorne, criar sessão para o usuário
            if resultado:
                session['usuario'] = resultado['usuario']
                session['nome'] = resultado['nome']
                return True
            else: 
                return False
        except mysql.connector.Error as err:
            # 5. Erro vindo do MySQL (acesso negado, query malformada, etc.)
            print("Erro MySQL:")
            print("Código:", err.errno)
            print("SQLSTATE:", err.sqlstate)
            print("Mensagem:", err.msg)
            return False
        
        except Exception as e:
            # 6. Outro erro qualquer (erro de lógica, conexão nula, etc.)
            print("Erro inesperado:")
            print(type(e))
            print(e)
            traceback.print_exc()
            return False
             
        finally:
            # Caso a conexão seja criada, ela pode ser fechada.
            # Sem isso, pode ter erro caso a conexão não seja criada.
            if 'conexao' in locals():
                conexao.close
