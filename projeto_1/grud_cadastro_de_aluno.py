import psycopg2
from datetime import datetime
import random


def conectar_banco():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="escola",
            user="postgres",
            password="250502"
        )
        print("Conexão bem sucedida!")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def obter_dados_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nome_do_pai = input("Digite o nome do pai: ")
    nome_da_mae = input("Digite o nome da mãe: ")
    while True:
        try:
            data_de_nascimento = datetime.strptime(
                input("Digite a data de nascimento do aluno (formato: dd-mm-yyyy): "), "%d-%m-%Y")
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite a data no formato dd-mm-yyyy.")
    while True:
        try:
            data_de_matricula = datetime.strptime(input("Digite a data de matrícula do aluno (formato: dd-mm-yyyy): "),
                                                  "%d-%m-%Y")
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite a data no formato dd-mm-yyyy.")
    ativo = input("O aluno está ativo? (S/N): ").strip().upper().startswith("S")
    sexo = input("Digite o sexo do aluno: ")
    naturalidade = input("Digite a naturalidade do aluno: ")
    email = input("Digite o email do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    rg = input("Digite o RG do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    celular = input("Digite o celular do aluno: ")
    serie = input("Digite a série do aluno: ")
    turma = input("Digite a turma do aluno: ")
    turno = input("Digite o turno do aluno: ")
    responsavel = input("Digite o responsável pelo aluno: ")
    observacao = input("Digite alguma observação sobre o aluno: ")

    return (
        nome, idade, nome_do_pai, nome_da_mae, data_de_nascimento, data_de_matricula,
        ativo, sexo, naturalidade, email, cpf, rg, telefone, celular, serie, turma,
        turno, responsavel, observacao
    )


#criar função para gerar_id aleatório com 9 digitos usando a biblioteca random

def gerar_id():
    return random.randint(100000000, 999999999)


def inserir_aluno(conn):
    try:
        cursor = conn.cursor()
        aluno_id = gerar_id()
        dados_aluno = obter_dados_aluno()
        cursor.execute("""
            INSERT INTO alunos (
                id_aluno, nome, idade, nome_do_pai, nome_da_mae, data_de_nascimento,
                data_de_matricula, ativo, sexo, naturalidade, email, cpf, rg,
                telefone, celular, serie, turma, turno, responsavel, observacao
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (aluno_id,) + dados_aluno)
        conn.commit()
        print("Aluno inserido com sucesso!")
    except (psycopg2.Error, ValueError) as e:
        print(f"Erro ao inserir aluno: {e}")
    finally:
        cursor.close()


def excluir_aluno(conn):
    try:
        cursor = conn.cursor()
        id_aluno = input("Digite o ID do aluno que deseja excluir: ")
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
        aluno = cursor.fetchone()
        if aluno:
            confirmacao = input(f"Tem certeza que deseja excluir o aluno '{aluno[1]}'? (Sim/Não): ").strip().upper()
            if confirmacao.startswith("S"):
                cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (id_aluno,))
                conn.commit()
                print("Aluno excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
        else:
            print("Aluno não encontrado.")
    except psycopg2.Error as e:
        print(f"Erro ao excluir aluno: {e}")
    finally:
        cursor.close()


def atualizar_aluno(conn):
    try:
        cursor = conn.cursor()
        id_aluno = input("Digite o ID do aluno que deseja atualizar: ")
        cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
        aluno = cursor.fetchone()
        if aluno:
            nome_campo = input("Digite o nome do campo que deseja atualizar: ")
            novo_valor = input(f"Digite o novo valor para {nome_campo}: ")
            cursor.execute(f"UPDATE alunos SET {nome_campo} = %s WHERE id_aluno = %s", (novo_valor, id_aluno))
            conn.commit()
            print("Aluno atualizado com sucesso!")
        else:
            print("Aluno não encontrado.")
    except psycopg2.Error as e:
        print(f"Erro ao atualizar aluno: {e}")
    finally:
        cursor.close()


def sair():
    print("Saindo...")


def consultar_alunos(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        return alunos
    except psycopg2.Error as e:
        print(f"Erro ao consultar alunos: {e}")


# Adicione a exibição dos resultados na função main
def main():
    conn = conectar_banco()
    if conn:
        opcoes_menu = {
            '1': inserir_aluno,
            '2': consultar_alunos,
            '3': atualizar_aluno,
            '4': excluir_aluno,
            '5': sair
        }
        try:
            while True:
                print("1 - Cadastrar Aluno")
                print("2 - Listar Alunos")
                print("3 - Atualizar Aluno")
                print("4 - Deletar Aluno")
                print("5 - Sair")
                opcao = input("Escolha uma opção: ")
                funcao = opcoes_menu.get(opcao)
                if funcao:
                    if opcao == '2':
                        alunos = funcao(conn)
                        for aluno in alunos:
                            print(aluno)  # Exibe cada aluno
                    else:
                        funcao(conn)
                else:
                    print("Opção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
        finally:
            conn.close()


if __name__ == '__main__':
    main()
