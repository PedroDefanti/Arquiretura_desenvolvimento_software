"""BUILDER (criacional): separa a construção de um objeto complexo da sua representação."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Computador:  # Produto
    cpu: str = ""
    ram_gb: int = 0
    armazenamento: str = ""
    gpu: str | None = None

    def __str__(self) -> str:
        gpu = self.gpu or "integrada"
        return f"PC[{self.cpu} | {self.ram_gb}GB RAM | {self.armazenamento} | GPU {gpu}]"


class ComputadorBuilder:  # Builder (interface fluente)
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> "ComputadorBuilder":
        self._pc = Computador()
        return self

    def com_cpu(self, cpu: str) -> "ComputadorBuilder":
        self._pc.cpu = cpu
        return self

    def com_ram(self, gb: int) -> "ComputadorBuilder":
        self._pc.ram_gb = gb
        return self

    def com_armazenamento(self, desc: str) -> "ComputadorBuilder":
        self._pc.armazenamento = desc
        return self

    def com_gpu(self, gpu: str) -> "ComputadorBuilder":
        self._pc.gpu = gpu
        return self

    def build(self) -> Computador:
        if not self._pc.cpu or not self._pc.ram_gb:
            raise ValueError("CPU e RAM são obrigatórias")
        pc, _ = self._pc, self.reset()
        return pc


class Diretor:  # Director: receitas prontas de construção
    def __init__(self, builder: ComputadorBuilder) -> None:
        self.builder = builder

    def pc_escritorio(self) -> Computador:
        return (self.builder.reset().com_cpu("Ryzen 5").com_ram(16)
                .com_armazenamento("SSD 512GB").build())

    def pc_gamer(self) -> Computador:
        return (self.builder.reset().com_cpu("Ryzen 9").com_ram(32)
                .com_armazenamento("SSD 2TB NVMe").com_gpu("RTX 4070").build())


if __name__ == "__main__":
    diretor = Diretor(ComputadorBuilder())
    print(diretor.pc_escritorio())
    print(diretor.pc_gamer())
    # Uso direto, sem o diretor:
    print(ComputadorBuilder().com_cpu("i3").com_ram(8).com_armazenamento("HD 1TB").build())