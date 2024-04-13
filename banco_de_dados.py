import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario", #Inserir seus dados, por segurança omiti os meus.
    password="sua_senha" #idem
)
cursor = conexao.cursor()


criar_bd = "CREATE DATABASE IF NOT EXISTS dados_pessoais"
cursor.execute(criar_bd)
cursor.execute("USE dados_pessoais")


criar_tabela = """
CREATE TABLE IF NOT EXISTS pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(100),
    idade INT,
    genero VARCHAR(10),
    nacionalidade VARCHAR(50),
    email VARCHAR(100),
    estado_civil VARCHAR(20),
    nome_pai VARCHAR(100),
    nome_mae VARCHAR(100)
)
"""
cursor.execute(criar_tabela)

# Inserir dados
pessoas_exemplo = [
    ("Aruk", 4, "Masculino", "Brasileiro", "aruk@gmail.com", "Solteiro", "Nayson", "Desconhecida"),
    ("Eevee", 3, "Masculino", "Brasileiro", "eevee@gmail.com", "Solteiro", "Nayson", "Desconhecida"),
    ("Meirivane", 53, "Feminino", "Brasileira", "meiry@gmail.com", "Divorciada", "Altino José", "Mª Beatriz")
]

inserir = "INSERT INTO pessoas (nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_pai, nome_mae) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(inserir, pessoas_exemplo)

# Atualizar pessoa
id_atualizar = 1
nova_idade = 5
nova_nacionalidade = "Alemão"
atualizar = "UPDATE pessoas SET idade = %s, nacionalidade = %s WHERE id = %s"
cursor.execute(atualizar, (nova_idade, nova_nacionalidade, id_atualizar))

# Remover pessoa
id_remover = 3
remover = "DELETE FROM pessoas WHERE id = %s"
cursor.execute(remover, (id_remover,))


conexao.commit()
cursor.close()
conexao.close()
