"""COMMAND (comportamental): encapsula uma requisição como objeto (permite desfazer/refazer)."""
from __future__ import annotations
from abc import ABC, abstractmethod


class Editor:  # Receiver
    def __init__(self) -> None:
        self.texto = ""


class Comando(ABC):  # Command
    @abstractmethod
    def executar(self) -> None: ...
    @abstractmethod
    def desfazer(self) -> None: ...


class Escrever(Comando):  # ConcreteCommand
    def __init__(self, editor: Editor, trecho: str) -> None:
        self.editor, self.trecho = editor, trecho

    def executar(self) -> None:
        self.editor.texto += self.trecho

    def desfazer(self) -> None:
        self.editor.texto = self.editor.texto[: -len(self.trecho)]


class Apagar(Comando):  # ConcreteCommand
    def __init__(self, editor: Editor, qtd: int) -> None:
        self.editor, self.qtd, self._apagado = editor, qtd, ""

    def executar(self) -> None:
        self._apagado = self.editor.texto[-self.qtd:]
        self.editor.texto = self.editor.texto[: -self.qtd]

    def desfazer(self) -> None:
        self.editor.texto += self._apagado


class Historico:  # Invoker
    def __init__(self) -> None:
        self._feitos: list[Comando] = []
        self._desfeitos: list[Comando] = []

    def executar(self, cmd: Comando) -> None:
        cmd.executar()
        self._feitos.append(cmd)
        self._desfeitos.clear()

    def desfazer(self) -> None:
        if self._feitos:
            cmd = self._feitos.pop()
            cmd.desfazer()
            self._desfeitos.append(cmd)

    def refazer(self) -> None:
        if self._desfeitos:
            cmd = self._desfeitos.pop()
            cmd.executar()
            self._feitos.append(cmd)


if __name__ == "__main__":
    ed, hist = Editor(), Historico()
    hist.executar(Escrever(ed, "Olá, "))
    hist.executar(Escrever(ed, "mundo!"))
    print(repr(ed.texto))          # 'Olá, mundo!'
    hist.executar(Apagar(ed, 6))
    print(repr(ed.texto))          # 'Olá, '
    hist.desfazer()
    print(repr(ed.texto))          # 'Olá, mundo!'
    hist.desfazer()
    print(repr(ed.texto))          # 'Olá, '
    hist.refazer()
    print(repr(ed.texto))          # 'Olá, mundo!'