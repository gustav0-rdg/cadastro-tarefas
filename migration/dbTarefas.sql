CREATE DATABASE IF NOT EXISTS dbTarefas;
USE dbTarefas;

CREATE TABLE tbUser(
	usuario VARCHAR(30) PRIMARY KEY,
    nome VARCHAR(30) not null,
    senha_usuario varchar(20) not null
    );

CREATE TABLE tbTarefas(
	id_tarefa int AUTO_INCREMENT PRIMARY KEY,
    titulo varchar(20) not null,
    descricao text not null,
    dataHora DATETIME
    );