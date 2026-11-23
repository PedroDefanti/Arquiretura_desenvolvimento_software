"""STRATEGY: cálculo do tempo de viagem conforme o método de transporte escolhido."""
from __future__ import annotations
from abc import ABC, abstractmethod


class EstrategiaTransporte(ABC):  # Strategy: contrato comum
    @property
    @abstractmethod
    def nome(self) -> str: ...

    @abstractmethod
    def calcular_tempo_minutos(self, distancia_km: float) -> float: ...


class Caminhada(EstrategiaTransporte):  # ConcreteStrategy: 5 km/h
    VELOCIDADE_KMH = 5.0
    nome = "Caminhada"

    def calcular_tempo_minutos(self, distancia_km: float) -> float:
        return distancia_km / self.VELOCIDADE_KMH * 60


class Bicicleta(EstrategiaTransporte):  # ConcreteStrategy: 15 km/h
    VELOCIDADE_KMH = 15.0
    nome = "Bicicleta"

    def calcular_tempo_minutos(self, distancia_km: float) -> float:
        return distancia_km / self.VELOCIDADE_KMH * 60


class Carro(EstrategiaTransporte):  # ConcreteStrategy: 60 km/h + 5 min para estacionar
    VELOCIDADE_KMH = 60.0
    TEMPO_ESTACIONAR_MIN = 5.0
    nome = "Carro"

    def calcular_tempo_minutos(self, distancia_km: float) -> float:
        return distancia_km / self.VELOCIDADE_KMH * 60 + self.TEMPO_ESTACIONAR_MIN


class Onibus(EstrategiaTransporte):  # ConcreteStrategy: 30 km/h + 10 min de espera
    VELOCIDADE_KMH = 30.0
    TEMPO_ESPERA_MIN = 10.0
    nome = "Ônibus"

    def calcular_tempo_minutos(self, distancia_km: float) -> float:
        return distancia_km / self.VELOCIDADE_KMH * 60 + self.TEMPO_ESPERA_MIN


class CalculadoraViagem:  # Context: guarda a estratégia e delega o cálculo
    def __init__(self, estrategia: EstrategiaTransporte) -> None:
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaTransporte) -> None:
        """Troca a estratégia em tempo de execução."""
        self._estrategia = estrategia

    @property
    def nome_estrategia(self) -> str:
        return self._estrategia.nome

    def calcular(self, distancia_km: float) -> float:
        if distancia_km < 0:
            raise ValueError("A distância não pode ser negativa")
        return self._estrategia.calcular_tempo_minutos(distancia_km)


def formatar(minutos: float) -> str:
    total = round(minutos)
    h, m = divmod(total, 60)
    return f"{h}h{m:02d}min" if h else f"{m}min"


class Principal:
    @staticmethod
    def main() -> None:
        # "Catálogo" de métodos: a chave simula a escolha do usuário
        metodos: dict[str, EstrategiaTransporte] = {
            "andando": Caminhada(),
            "bicicleta": Bicicleta(),
            "carro": Carro(),
            "onibus": Onibus(),
        }
        distancia_km = 10.0
        calculadora = CalculadoraViagem(metodos["andando"])

        print(f"Viagem de {distancia_km:.1f} km\n")
        for escolha, estrategia in metodos.items():
            calculadora.definir_estrategia(estrategia)  # troca em tempo de execução
            tempo = formatar(calculadora.calcular(distancia_km))
            print(f"Escolha: {escolha:<10} -> {calculadora.nome_estrategia:<10} | tempo estimado: {tempo}")

        # Nova estratégia sem alterar nenhuma classe existente (aberto/fechado)
        class Patinete(EstrategiaTransporte):
            nome = "Patinete"

            def calcular_tempo_minutos(self, distancia_km: float) -> float:
                return distancia_km / 20.0 * 60

        print("\nAdicionando uma nova estratégia (Patinete, 20 km/h):")
        calculadora.definir_estrategia(Patinete())
        print(f"{calculadora.nome_estrategia} -> {formatar(calculadora.calcular(distancia_km))}")


if __name__ == "__main__":
    Principal.main()