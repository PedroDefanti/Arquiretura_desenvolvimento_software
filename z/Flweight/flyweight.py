"""FLYWEIGHT (estrutural): compartilha estado intrínseco para economizar memória."""
from __future__ import annotations


class TipoArvore:  # Flyweight: estado INTRÍNSECO (compartilhado, imutável)
    def __init__(self, nome: str, cor: str, textura: str) -> None:
        self.nome, self.cor, self.textura = nome, cor, textura

    def desenhar(self, x: int, y: int) -> str:  # x, y = estado EXTRÍNSECO
        return f"{self.nome} ({self.cor}) em ({x},{y})"


class FabricaTipos:  # Flyweight Factory: garante o compartilhamento
    _cache: dict[tuple, TipoArvore] = {}

    @classmethod
    def obter(cls, nome: str, cor: str, textura: str) -> TipoArvore:
        chave = (nome, cor, textura)
        if chave not in cls._cache:
            cls._cache[chave] = TipoArvore(nome, cor, textura)
        return cls._cache[chave]

    @classmethod
    def total(cls) -> int:
        return len(cls._cache)


class Arvore:  # Contexto: guarda só o estado extrínseco + referência ao flyweight
    def __init__(self, x: int, y: int, tipo: TipoArvore) -> None:
        self.x, self.y, self.tipo = x, y, tipo

    def desenhar(self) -> str:
        return self.tipo.desenhar(self.x, self.y)


class Floresta:
    def __init__(self) -> None:
        self.arvores: list[Arvore] = []

    def plantar(self, x, y, nome, cor, textura) -> None:
        self.arvores.append(Arvore(x, y, FabricaTipos.obter(nome, cor, textura)))


if __name__ == "__main__":
    f = Floresta()
    for i in range(1000):
        f.plantar(i, i * 2, "Pinheiro", "verde-escuro", "pinheiro.png")
        f.plantar(i, i * 3, "Carvalho", "verde", "carvalho.png")
    print(f.arvores[0].desenhar())
    print(f"Árvores: {len(f.arvores)} | Objetos TipoArvore: {FabricaTipos.total()}")