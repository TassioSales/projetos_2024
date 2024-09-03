class Tarefa:
    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def __str__(self):
        return f"Título: {self.titulo}\nDescrição: {self.descricao}\nConcluída: {self.concluida}"


class GestorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def marcar_como_concluida(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.concluida = True

    def remover_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                self.tarefas.remove(tarefa)

    def listar_tarefas(self):
        pendentes = []
        concluidas = []
        for tarefa in self.tarefas:
            if not tarefa.concluida:
                pendentes.append(tarefa)
            else:
                concluidas.append(tarefa)
        return pendentes, concluidas

    def execute(self):
        while True:
            print("1. Adicionar tarefa")
            print("2. Marcar tarefa como concluída")
            print("3. Remover tarefa")
            print("4. Listar tarefas")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                titulo = input("Título da tarefa: ")
                descricao = input("Descrição da tarefa: ")
                tarefa = Tarefa(titulo, descricao)
                self.adicionar_tarefa(tarefa)
            elif opcao == "2":
                titulo = input("Título da tarefa: ")
                self.marcar_como_concluida(titulo)
            elif opcao == "3":
                titulo = input("Título da tarefa: ")
                self.remover_tarefa(titulo)
            elif opcao == "4":
                pendentes, concluidas = self.listar_tarefas()
                print("Tarefas pendentes:")
                for tarefa in pendentes:
                    print(tarefa)
                print("Tarefas concluídas:")
                for tarefa in concluidas:
                    print(tarefa)
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    gestor = GestorDeTarefas()
    gestor.execute()
