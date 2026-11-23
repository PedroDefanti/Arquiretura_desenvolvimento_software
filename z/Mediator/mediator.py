"""MEDIATOR (comportamental): centraliza a comunicação entre objetos, reduzindo o acoplamento."""
from __future__ import annotations
from abc import ABC, abstractmethod


class Mediador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str, remetente: "Usuario") -> None: ...


class Usuario:  # Colleague: só conhece o mediador, nunca os outros usuários
    def __init__(self, nome: str, mediador: Mediador) -> None:
        self.nome, self.mediador = nome, mediador

    def enviar(self, mensagem: str) -> None:
        print(f"[{self.nome}] envia: {mensagem}")
        self.mediador.enviar(mensagem, self)

    def receber(self, mensagem: str, de: "Usuario") -> None:
        print(f"   {self.nome} recebeu de {de.nome}: {mensagem}")


class SalaDeChat(Mediador):  # ConcreteMediator
    def __init__(self) -> None:
        self._usuarios: list[Usuario] = []

    def entrar(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def enviar(self, mensagem: str, remetente: Usuario) -> None:
        for u in self._usuarios:
            if u is not remetente:
                u.receber(mensagem, remetente)


if __name__ == "__main__":
    sala = SalaDeChat()
    ana, bia, caio = (Usuario(n, sala) for n in ("Ana", "Bia", "Caio"))
    for u in (ana, bia, caio):
        sala.entrar(u)
    ana.enviar("Bom dia, pessoal!")
    caio.enviar("Bom dia, Ana!")