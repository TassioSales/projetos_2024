import psycopg2


def criar_tabela_alunos():
    """
    A function to create a table in the database for storing student information. It establishes a connection to the
    database, creates a table named 'alunos' with various columns such as name, age, parent's names, dates,
    contact information, and other details. If successful, it prints a success message and returns True. If an
    exception occurs, it prints the error message and returns False.
    """
    try:
        conn = psycopg2.connect(host="localhost", database="escola", user="postgres", password="250502")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE alunos (
            nome VARCHAR(255),
            idade INTEGER,
            nome_do_pai VARCHAR(255),
            nome_da_mae VARCHAR(255),
            data_de_nascimento DATE,
            data_de_matricula DATE,
            ativo BOOLEAN,
            sexo VARCHAR(255),
            naturalidade VARCHAR(255),
            email VARCHAR(255),
            cpf VARCHAR(255),
            rg VARCHAR(255),
            telefone VARCHAR(255),
            celular VARCHAR(255),
            serie VARCHAR(255),
            turma VARCHAR(255),
            turno VARCHAR(255),
            responsavel VARCHAR(255),
            observacao TEXT
        )""")
        conn.commit()
        cursor.close()
        conn.close()
        print("Tabela criada com sucesso!")
        return True
    except Exception as e:
        print(e)
        return False


#verifica se a tabela foi criada
def verifica_tabela_alunos():
    """
    Function to verify the existence of the 'alunos' table in the 'escola' database.
    Connects to the database and checks if the table exists.
    Returns True if the table exists, False otherwise.
    """
    try:
        conn = psycopg2.connect(host="localhost", database="escola", user="postgres", password="250502")
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_name = 'alunos')")
        result = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        print("Erro ao verificar a tabela: ", e)
        return False



def select_tabela_alunos():
    """
    This function connects to the database, retrieves all rows from the 'alunos' table,
    prints the column names, and returns the result. If an exception occurs, it prints
    the error and returns False.
    """
    try:
        conn = psycopg2.connect(host="localhost", database="escola", user="postgres", password="250502")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alunos")
        #mostra nome das colunas
        print("Nome das colunas da tabela alunos:")
        for i in cursor.description:
            print(i[0])
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        print("Erro ao verificar a tabela: ", e)
        return False


if __name__ == '__main__':
    if not verifica_tabela_alunos():
        criar_tabela_alunos()
        print(select_tabela_alunos())
    else:
        print("Tabela ja existe")
