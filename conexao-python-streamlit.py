import streamlit as st
import mysql.connector

# Estabelecendo a conexão com o banco de dados MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

# Criando uma tabela no banco de dados
def create_table():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255))")
    connection.commit()

# Inserindo dados na tabela
def insert_data(nome, email):
    cursor = connection.cursor()
    query = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    values = (nome, email)
    cursor.execute(query, values)
    connection.commit()

# Lendo dados da tabela
def read_data():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    result = cursor.fetchall()
    return result

# Interface do Streamlit
st.title("Aplicação com Banco de Dados")

# Criando a tabela (caso não exista)
create_table()

# Formulário para inserir dados na tabela
nome = st.text_input("Nome")
email = st.text_input("Email")
if st.button("Adicionar"):
    insert_data(nome, email)
    st.success("Dados inseridos com sucesso!")

# Exibindo os dados da tabela
usuarios = read_data()
st.table(usuarios)
