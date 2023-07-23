import mysql.connector

'''
conexao = mysql.connector.connect(
    host="localhost", user="root", password="", database="jdlivraria"
)
cursor = conexao.cursor()
print("Banco conectado!")
'''
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # Endereço do servidor do banco de dados
    'database': 'jdlivraria'
}

try:
    # Estabelece a conexão com o banco de dados
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Conexão ao banco de dados estabelecida.")

        # A partir desse ponto, você pode executar operações no banco de dados usando o objeto 'connection'.

        # Por exemplo, para consultar os registros da tabela "usuarios":
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuarios = olavo")
        dados = cursor.fetchall()
        print(dados)
        # Exibindo os resultados da consulta
        '''for (id, usuario, senha) in cursor:
            print(f"ID: {id}, Usuário: {usuario}, Senha: {senha}")'''

        # Fechando o cursor e a conexão
        cursor.close()
        connection.close()
        print("Conexão ao banco de dados encerrada.")

except mysql.connector.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")