import copy


class Tarefa:
    def __init__(self, titulo: str, descricao: str):
        self._titulo = titulo
        self._descricao = descricao

    def getTitulo(self) -> str:
        return self._titulo

    def setTitulo(self, titulo: str):
        self._titulo = titulo

    def getDescricao(self) -> str:
        return self._descricao

    def setDescricao(self, descricao: str):
        self._descricao = descricao

    def __str__(self):
        return f"Título: {self._titulo} | Descrição: {self._descricao}"



class TarefaMemento:
    def __init__(self, tarefas: list[Tarefa]):

        self._tarefas_snapshot = copy.deepcopy(tarefas)

    def get_tarefas(self) -> list[Tarefa]:
        return self._tarefas_snapshot



class Zelador:
    def __init__(self):
        self._historico = []

    def salvar_estado(self, memento: TarefaMemento):
        self._historico.append(memento)

    def desfazer(self) -> TarefaMemento | None:
        if not self._historico:
            return None
        return self._historico.pop()



class GerenciadorTarefas:
    def __init__(self):
        self._tarefas = []

    def adicionar(self, tarefa: Tarefa, zelador: Zelador):

        zelador.salvar_estado(TarefaMemento(self._tarefas))
        self._tarefas.append(tarefa)
        print(f"[Adicionado] Tarefa '{tarefa.getTitulo()}' incluída.")

    def editar(self, indice: int, novo_titulo: str, nova_descricao: str, zelador: Zelador):
        if 0 <= indice < len(self._tarefas):

            zelador.salvar_estado(TarefaMemento(self._tarefas))
            self._tarefas[indice].setTitulo(novo_titulo)
            self._tarefas[indice].setDescricao(nova_descricao)
            print(f"[Editado] Tarefa do índice {indice} atualizada.")
        else:
            print("[Erro] Índice inválido para edição.")

    def remover(self, indice: int, zelador: Zelador):
        if 0 <= indice < len(self._tarefas):

            zelador.salvar_estado(TarefaMemento(self._tarefas))
            removida = self._tarefas.pop(indice)
            print(f"[Removido] Tarefa '{removida.getTitulo()}' excluída.")
        else:
            print("[Erro] Índice inválido para remoção.")
            
    def desfazer(self, zelador: Zelador):
        memento_anterior = zelador.desfazer()
        if memento_anterior:

            self._tarefas = copy.deepcopy(memento_anterior.get_tarefas())
            print("[Desfazer] Ação desfeita com sucesso!")
        else:
            print("[Aviso] Não há ações para desfazer.")

    def listar(self):
     
        if not self._tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(self._tarefas):
                print(f"[{i}] {tarefa}")




if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    zelador = Zelador()


    t1 = Tarefa("Estudar Python", "Aprender sobre o padrão Memento")
    gerenciador.adicionar(t1, zelador)
    gerenciador.listar()
    t2 = Tarefa("Fazer compras", "Comprar leite e pão")
    gerenciador.adicionar(t2, zelador)
    gerenciador.listar()
    gerenciador.editar(0, "Estudar Design Patterns", "Estudar Memento, Command e Observer", zelador)
    gerenciador.listar()
    gerenciador.remover(1, zelador)
    gerenciador.listar()



    print(">>> Desfazendo a última ação (Remoção da tarefa de compras)...")
    gerenciador.desfazer(zelador)
    gerenciador.listar()

    print(">>> Desfazendo a ação anterior (Edição da primeira tarefa)...")
    gerenciador.desfazer(zelador)
    gerenciador.listar()

    print(">>> Desfazendo a adição da segunda tarefa...")
    gerenciador.desfazer(zelador)
    gerenciador.listar()