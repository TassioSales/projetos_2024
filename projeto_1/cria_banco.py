import psycopg2
from psycopg2 import Error


def conectar_bd():
    """
    Função que estabelece uma conexão com o banco de dados utilizando a biblioteca psycopg2.
    Retorna o objeto de conexão se for bem-sucedido, caso contrário, imprime o erro e retorna None.
    """
    try:
        config = {
            'host': 'localhost',
            'database': 'postgres',
            'user': 'postgres',
            'password': '250502'
        }
        conn = psycopg2.connect(**config)
        print("Conexão estabelecida com sucesso")
        return conn
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


def desconectar_bd(conn):
    """
    Fecha a conexão com o banco de dados e imprime uma mensagem de sucesso.
    """
    try:
        if conn:
            conn.close()
            print("Conexão encerrada com sucesso")
    except Error as e:
        print("Erro ao desconectar do banco de dados:", e)


def criar_banco():
    """
    Função para criar um banco de dados chamado 'escola'.
    """
    try:
        conn = conectar_bd()
        if conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                cursor.execute("CREATE DATABASE escola")
            print("Banco de dados criado com sucesso")
    except Error as e:
        print("Erro ao criar o banco de dados:", e)
    finally:
        desconectar_bd(conn)


def verificar_banco():
    """
    Função para verificar se o banco de dados 'escola' existe.
    Retorna True se o banco de dados existe, False caso contrário.
    """
    try:
        conn = conectar_bd()
        if conn:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT EXISTS(SELECT * FROM pg_catalog.pg_database WHERE datname = 'escola')")
                    resultado = cursor.fetchone()[0]
            return resultado
    except Error as e:
        print("Erro ao verificar o banco de dados:", e)
    finally:
        desconectar_bd(conn)
        return False


if __name__ == '__main__':
    if not verificar_banco():
        criar_banco()
    else:
        print("O banco de dados já existe")
