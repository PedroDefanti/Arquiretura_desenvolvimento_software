"""STATE (comportamental): o objeto muda de comportamento quando seu estado interno muda."""
from __future__ import annotations
from abc import ABC


class Estado(ABC):  # State: comportamento padrão = operação inválida
    nome = "?"

    def pagar(self, pedido: "Pedido") -> None:
        print(f"  ✗ Não é possível pagar no estado {self.nome}")

    def enviar(self, pedido: "Pedido") -> None:
        print(f"  ✗ Não é possível enviar no estado {self.nome}")

    def entregar(self, pedido: "Pedido") -> None:
        print(f"  ✗ Não é possível entregar no estado {self.nome}")

    def cancelar(self, pedido: "Pedido") -> None:
        print(f"  ✗ Não é possível cancelar no estado {self.nome}")


class Criado(Estado):
    nome = "Criado"
    def pagar(self, p): p.estado = Pago(); print("  ✓ Pagamento confirmado")
    def cancelar(self, p): p.estado = Cancelado(); print("  ✓ Pedido cancelado")


class Pago(Estado):
    nome = "Pago"
    def enviar(self, p): p.estado = Enviado(); print("  ✓ Pedido enviado")
    def cancelar(self, p): p.estado = Cancelado(); print("  ✓ Cancelado com estorno")


class Enviado(Estado):
    nome = "Enviado"
    def entregar(self, p): p.estado = Entregue(); print("  ✓ Pedido entregue")


class Entregue(Estado):
    nome = "Entregue"


class Cancelado(Estado):
    nome = "Cancelado"


class Pedido:  # Context
    def __init__(self) -> None:
        self.estado: Estado = Criado()

    def pagar(self): self.estado.pagar(self)
    def enviar(self): self.estado.enviar(self)
    def entregar(self): self.estado.entregar(self)
    def cancelar(self): self.estado.cancelar(self)

    def __str__(self) -> str:
        return f"Pedido({self.estado.nome})"


if __name__ == "__main__":
    p = Pedido()
    print(p)
    p.enviar()      # inválido: ainda não foi pago
    p.pagar();   print(p)
    p.enviar();  print(p)
    p.cancelar()    # inválido: já foi enviado
    p.entregar(); print(p)