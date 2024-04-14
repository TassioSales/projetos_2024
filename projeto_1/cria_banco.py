#função para conectar ao banco de dados postgresql
import psycopg2


def conecta_bd():
    """
    A function that establishes a connection to the database using the psycopg2 library.
    It attempts to connect to a database with the provided credentials and returns the connection object if successful,
    otherwise, it prints the error and returns None.
    """
    global conn
    try:
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="250502")
        #verifica se a conexão foi efetuada com sucesso
        print("Conexão efetuada com sucesso")
        return conn
    except Exception as e:
        print("Erro: ", e)
        return None



def desconecta_bd():
    """
    Closes the database connection and prints a success message.
    """
    global conn
    conn.close()
    print("Conexão encerrada com sucesso")

def criar_banco():
    """
    Function to create a database. It connects to the database, sets autocommit to True, creates a database named
    'escola', disconnects from the database, and prints a success message. If an exception occurs, it prints an error
    message with the exception details.
    """
    try:
        conn = conecta_bd()
        cursor = conn.cursor()
        # Configura autocommit para True
        conn.autocommit = True
        cursor.execute("CREATE DATABASE escola")
        desconecta_bd()
        print("Banco de dados criado com sucesso")
    except Exception as e:
        print("Erro ao criar o banco de dados: ", e)


def verifica_banco():
    """
    Function to verify the existence of a database schema named 'escola'.
    """
    try:
        conn = conecta_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS(SELECT * FROM information_schema.schemata WHERE schema_name = 'escola')")
        resultado = cursor.fetchone()[0]
        cursor.close()  # Fechando explicitamente o cursor
        desconecta_bd()
        return resultado
    except Exception as e:
        print("Erro ao verificar o banco de dados: ", e)
        return False



if __name__ == '__main__':
    if not verifica_banco():
        criar_banco()
    else:
        print("Banco de dados ja existe")
