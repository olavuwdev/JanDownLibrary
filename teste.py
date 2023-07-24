import mysql.connector

# Configurações da conexão com o banco de dados
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # Endereço do servidor do banco de dados
    'database': 'jdlivraria',
    'raise_on_warnings': True
}

# Dados dos livros a serem inseridos
livros_para_inserir = [
    ("Código Limpo", "Robert C. Martin", "Alta Books", 59.90, "Livro sobre boas práticas de programação com exemplos em Python."),
    ("O Hobbit", "J.R.R. Tolkien", "HarperCollins", 39.90, "Uma história de aventuras em um mundo de fantasia."),
    ("Python Fluente", "Luciano Ramalho", "Novatec", 79.90, "Guia avançado para a linguagem Python."),
    ("A Menina que Roubava Livros", "Markus Zusak", "Intrínseca", 29.90, "A história de uma jovem alemã durante a Segunda Guerra Mundial."),
    ("A Origem das Espécies", "Charles Darwin", "L&PM Editores", 45.00, "Obra sobre a teoria da evolução."),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Agir", 19.90, "Um livro que encanta leitores de todas as idades."),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", "Martins Fontes", 120.00, "Trilogia épica de fantasia."),
    ("O Código Da Vinci", "Dan Brown", "Arqueiro", 29.90, "Mistério e conspiração na busca pelo Santo Graal."),
    ("1984", "George Orwell", "Companhia das Letras", 39.90, "Distopia sobre um regime totalitário."),
    ("O Alquimista", "Paulo Coelho", "Rocco", 24.90, "Jornada de autoconhecimento."),
    ("Dom Casmurro", "Machado de Assis", "Martin Claret", 14.90, "Clássico da literatura brasileira."),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Rocco", 39.90, "Primeiro livro da série de fantasia."),
    ("Crime e Castigo", "Fiódor Dostoiévski", "Nova Fronteira", 49.90, "Estudo psicológico de um assassinato."),
    ("A Metamorfose", "Franz Kafka", "Companhia das Letras", 19.90, "Novela sobre a transformação de um homem em inseto."),
    ("Anna Karenina", "Liev Tolstói", "Nova Fronteira", 59.90, "História de amor e tragédia na Rússia do século XIX."),
    ("O Pequeno Livro das Sementes", "Ruth Kassinger", "Sextante", 39.90, "Exploração do mundo das sementes."),
    ("A Guerra dos Tronos", "George R.R. Martin", "LeYa", 49.90, "Início da série de fantasia 'As Crônicas de Gelo e Fogo'."),
    ("Eu Sou Malala", "Malala Yousafzai", "Companhia das Letras", 29.90, "Autobiografia da ativista paquistanesa."),
    ("Sapiens - Uma Breve História da Humanidade", "Yuval Noah Harari", "L&PM Editores", 59.90, "Visão da história humana."),
    ("A Coragem de Ser Imperfeito", "Brené Brown", "Sextante", 34.90, "Livro sobre vulnerabilidade e imperfeição."),
]

try:
    # Estabelece a conexão com o banco de dados
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Conexão ao banco de dados estabelecida.")

        # Inserindo os livros na tabela
        cursor = connection.cursor()
        sql = '''INSERT INTO livros (titulo, autor, editora, preco, descricao) VALUES (%s, %s, %s, %s, %s)'''
        cursor.executemany(sql, livros_para_inserir)
        connection.commit()

        print("Livros cadastrados com sucesso.")

        # Fechando o cursor e a conexão
        cursor.close()
        connection.close()
        print("Conexão ao banco de dados encerrada.")

except mysql.connector.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
print()