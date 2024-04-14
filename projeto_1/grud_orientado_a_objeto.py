import psycopg2
from datetime import datetime

class AlunoManager:
    def __init__(self, conn):
        self.conn = conn

    def inserir_aluno(self):
        try:
            cursor = self.conn.cursor()
            aluno_id = self.gerar_id()
            dados_aluno = self.obter_dados_aluno()
            cursor.execute("""
                INSERT INTO alunos (
                    id_aluno, nome, idade, nome_do_pai, nome_da_mae, data_de_nascimento,
                    data_de_matricula, ativo, sexo, naturalidade, email, cpf, rg,
                    telefone, celular, serie, turma, turno, responsavel, observacao
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (aluno_id,) + dados_aluno)
            self.conn.commit()
            print("Aluno inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir aluno: {e}")
            self.conn.rollback()
        finally:
            cursor.close()

    def obter_dados_aluno(self):
        nome = input("Digite o nome do aluno: ")
        idade = self.obter_inteiro("Digite a idade do aluno: ")
        nome_do_pai = input("Digite o nome do pai: ")
        nome_da_mae = input("Digite o nome da mãe: ")
        data_de_nascimento = self.obter_data("Digite a data de nascimento do aluno (formato: dd-mm-yyyy): ")
        data_de_matricula = self.obter_data("Digite a data de matrícula do aluno (formato: dd-mm-yyyy): ")
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

    def gerar_id(self):
        # Lógica para gerar um ID único para o aluno
        return random.randint(1, 1000000)  # Exemplo simples, substitua pela lógica real

    def consultar_alunos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM alunos")
            alunos = cursor.fetchall()
            if alunos:
                print("Listagem de Alunos:")
                print("+---------+------------+------+---------+")
                print("| ID      | Nome       | Idade| Ativo   |")
                print("+---------+------------+------+---------+")
                for aluno in alunos:
                    aluno_id, nome, idade, ativo = aluno[0], aluno[3], aluno[4], "Sim" if aluno[9] else "Não"
                    print(f"| {aluno_id:<8}| {nome:<11}| {idade:<5}| {ativo:<8}|")
                print("+---------+------------+------+---------+")
            else:
                print("Não há alunos cadastrados.")
        except Exception as e:
            print(f"Erro ao consultar alunos: {e}")
        finally:
            cursor.close()

    def excluir_aluno(self):
        try:
            cursor = self.conn.cursor()
            id_aluno = input("Digite o ID do aluno que deseja excluir: ")
            cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
            aluno = cursor.fetchone()
            if aluno:
                confirmacao = input(f"Tem certeza que deseja excluir o aluno '{aluno[3]}'? (Sim/Não): ").strip().upper()
                if confirmacao.startswith("S"):
                    cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (id_aluno,))
                    self.conn.commit()
                    print("Aluno excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Aluno não encontrado.")
        except Exception as e:
            print(f"Erro ao excluir aluno: {e}")
        finally:
            cursor.close()

    def atualizar_aluno(self):
        try:
            cursor = self.conn.cursor()
            id_aluno = input("Digite o ID do aluno que deseja atualizar: ")
            cursor.execute("SELECT * FROM alunos WHERE id_aluno = %s", (id_aluno,))
            aluno = cursor.fetchone()
            if aluno:
                print("Opções de colunas disponíveis para atualização:")
                colunas = [desc[0] for desc in cursor.description]
                for idx, coluna in enumerate(colunas[2:], start=1):  # Ignorando id_aluno e nome
                    print(f"{idx} - {coluna}")
                opcao = self.obter_inteiro("Escolha o número da coluna que deseja atualizar: ")
                if 1 <= opcao <= len(colunas) - 2:
                    nome_campo = colunas[opcao + 1]  # +1 para compensar o deslocamento do índice
                    valor_atual = aluno[opcao + 1]  # +1 para compensar o deslocamento do índice
                    print(f"Valor atual para {nome_campo}: {valor_atual}")
                    novo_valor = input(f"Digite o novo valor para {nome_campo}: ")
                    cursor.execute(f"UPDATE alunos SET {nome_campo} = %s WHERE id_aluno = %s", (novo_valor, id_aluno))
                    self.conn.commit()
                    print("Aluno atualizado com sucesso!")
                else:
                    print("Opção inválida.")
            else:
                print("Aluno não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar aluno: {e}")
        finally:
            cursor.close()

    @staticmethod
    def obter_inteiro(mensagem):
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    @staticmethod
    def obter_data(mensagem):
        while True:
            try:
                return datetime.strptime(input(mensagem), "%d-%m-%Y")
            except ValueError:
                print("Formato de data inválido. Por favor, digite a data no formato dd-mm-yyyy.")

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
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def sair():
    print("Saindo...")

def main():
    conn = conectar_banco()
    if conn:
        manager = AlunoManager(conn)
        opcoes_menu = {
            '1': manager.inserir_aluno,
            '2': manager.consultar_alunos,
            '3': manager.atualizar_aluno,
            '4': manager.excluir_aluno,
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
                    funcao()
                else:
                    print("Opção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
        finally:
            conn.close()

if __name__ == '__main__':
    main()
