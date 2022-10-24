import sqlite3
conexao = sqlite3.connect('banco_dados')

cursor = conexao.cursor()

#cursor.execute('CREATE TABLE jogadores(id INT NOT NULL,nome VARCHAR(100),cpf VARCHAR(11)UNIQUE,PRIMARY KEY(id));')
#cursor.execute('CREATE TABLE personagens(id_personagens INT, nome VARCHAR(100), habilidades VARCHAR(100), equipamentos VARCHAR(100), PRIMARY KEY(id_personagens), FOREIGN KEY(id_personagens) REFERENCES jogadores(id));')
#cursor.execute('INSERT INTO jogadores (id, nome, cpf) VALUES (2, "Kenji", "321");')

id = input("Digite seu id: ")
nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
RG = input("Digite seu RG: ")

dados = [id, nome, cpf, RG]
sql_inserir = "INSERT INTO jogadores (id, nome, cpf, RG) VALUES (?, ?, ?, ?)"
cursor.execute (sql_inserir, dados)

conexao.commit()
conexao.close