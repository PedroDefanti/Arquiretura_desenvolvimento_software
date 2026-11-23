"""TEMPLATE METHOD: gerenciador de tarefas com exibição por data de criação ou por prioridade."""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import IntEnum


class Prioridade(IntEnum):
    ALTA = 1      # menor valor = mais urgente (facilita a ordenação)
    MEDIA = 2
    BAIXA = 3

    def __str__(self) -> str:
        return {"ALTA": "Alta", "MEDIA": "Média", "BAIXA": "Baixa"}[self.name]


@dataclass
class Tarefa:
    nome: str
    prioridade: Prioridade
    data_criacao: datetime = field(default_factory=datetime.now)


class GerenciadorTarefas(ABC):
    """Classe base: define o esqueleto do algoritmo de exibição (Template Method)."""

    def __init__(self, tarefas: list[Tarefa] | None = None) -> None:
        # Lista compartilhada: várias estratégias de exibição podem usar as mesmas tarefas
        self._tarefas: list[Tarefa] = tarefas if tarefas is not None else []

    # ---- operações comuns (iguais para todas as subclasses) ----
    def adicionar(self, tarefa: Tarefa) -> None:
        self._tarefas.append(tarefa)

    def remover(self, nome: str) -> bool:
        for t in self._tarefas:
            if t.nome == nome:
                self._tarefas.remove(t)
                return True
        return False

    def listar(self) -> list[Tarefa]:
        return list(self._tarefas)

    # ---- TEMPLATE METHOD: sequência fixa, não sobrescrever ----
    def exibir(self) -> None:
        self._exibir_cabecalho()                     # passo 1 (hook)
        tarefas = self._ordenar(self.listar())       # passo 2 (abstrato: subclasses decidem)
        if not tarefas:
            print("(nenhuma tarefa cadastrada)")
        for t in tarefas:                            # passo 3 (comum)
            print(self._formatar(t))
        print()

    # ---- passo específico: obrigatório nas subclasses ----
    @abstractmethod
    def _ordenar(self, tarefas: list[Tarefa]) -> list[Tarefa]: ...

    # ---- passos comuns / hooks (subclasses podem sobrescrever) ----
    def _exibir_cabecalho(self) -> None:
        print("=== Tarefas ===")

    def _formatar(self, t: Tarefa) -> str:
        return (f"- Tarefa: {t.nome} - Data de criação: "
                f"{t.data_criacao:%d/%m/%Y %H:%M} - Prioridade: {t.prioridade}")


class GerenciadorPorData(GerenciadorTarefas):
    def _ordenar(self, tarefas: list[Tarefa]) -> list[Tarefa]:
        return sorted(tarefas, key=lambda t: t.data_criacao)

    def _exibir_cabecalho(self) -> None:
        print("=== Tarefas ordenadas por DATA DE CRIAÇÃO ===")


class GerenciadorPorPrioridade(GerenciadorTarefas):
    def _ordenar(self, tarefas: list[Tarefa]) -> list[Tarefa]:
        # desempate pela data de criação
        return sorted(tarefas, key=lambda t: (t.prioridade, t.data_criacao))

    def _exibir_cabecalho(self) -> None:
        print("=== Tarefas ordenadas por PRIORIDADE ===")


class Principal:
    @staticmethod
    def main() -> None:
        tarefas: list[Tarefa] = []  # mesma lista usada pelos dois gerenciadores
        por_data = GerenciadorPorData(tarefas)
        por_prioridade = GerenciadorPorPrioridade(tarefas)

        por_data.adicionar(Tarefa("Estudar Template Method", Prioridade.ALTA,   datetime(2026, 11, 20, 9, 0)))
        por_data.adicionar(Tarefa("Entregar relatório",       Prioridade.MEDIA, datetime(2026, 11, 21, 14, 30)))
        por_data.adicionar(Tarefa("Organizar planilha",       Prioridade.BAIXA, datetime(2026, 11, 19, 8, 15)))
        por_data.adicionar(Tarefa("Corrigir bug do login",    Prioridade.ALTA,  datetime(2026, 11, 22, 17, 45)))

        # Mesmo método exibir(), critérios diferentes: quem decide é a subclasse
        for gerenciador in (por_data, por_prioridade):
            gerenciador.exibir()

        print(">> Removendo 'Organizar planilha'...\n")
        por_prioridade.remover("Organizar planilha")
        for gerenciador in (por_data, por_prioridade):
            gerenciador.exibir()


if __name__ == "__main__":
    Principal.main()