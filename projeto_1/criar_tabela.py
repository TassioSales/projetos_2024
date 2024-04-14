import psycopg2


def conectar():
    """
    Função para conectar ao banco de dados PostgreSQL.
    Retorna a conexão.
    """
    connection_string = "host=localhost dbname=escola user=postgres password=250502"
    try:
        conn = psycopg2.connect(connection_string)
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


def criar_tabela_alunos(conn):
    """
    Função para criar a tabela 'alunos' no banco de dados.
    Retorna True se a tabela foi criada com sucesso, False caso contrário.
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (
                id_aluno SERIAL PRIMARY KEY,
                cpf VARCHAR(255) UNIQUE,
                rg VARCHAR(255) UNIQUE,
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
                telefone VARCHAR(255),
                celular VARCHAR(255),
                serie VARCHAR(255),
                turma VARCHAR(255),
                turno VARCHAR(255),
                responsavel VARCHAR(255),
                observacao TEXT
            )""")
            conn.commit()
        print("Tabela 'alunos' criada com sucesso!")
        return True
    except psycopg2.Error as e:
        print("Erro ao criar tabela 'alunos':", e)
        return False


def verificar_tabela(conn):
    """
    Função para verificar se a tabela 'alunos' existe no banco de dados.
    Retorna True se a tabela existe, False caso contrário.
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_name = 'alunos')")
            result = cursor.fetchone()[0]
        return result
    except psycopg2.Error as e:
        print("Erro ao verificar a tabela:", e)
        return False


def selecionar_alunos(conn):
    """
    Função para selecionar todos os registros da tabela 'alunos'.
    Retorna os registros ou None se ocorrer um erro.
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM alunos")
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            print("Nome das colunas da tabela alunos:")
            print(column_names)
        return rows
    except psycopg2.Error as e:
        print("Erro ao selecionar alunos:", e)
        return None


if __name__ == '__main__':
    conn = conectar()
    if conn:
        if not verificar_tabela(conn):
            if criar_tabela_alunos(conn):
                alunos = selecionar_alunos(conn)
                if alunos:
                    print(alunos)
        else:
            print("A tabela 'alunos' já existe.")
        conn.close()
