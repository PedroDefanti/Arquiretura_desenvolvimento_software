from abc import ABC, abstractmethod



class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass


class Sujeito(ABC):
    def __init__(self):
        self._observadores: list[Observer] = []

    def adicionar_observador(self, obs: Observer):
        if obs not in self._observadores:
            self._observadores.append(obs)

    def remover_observador(self, obs: Observer):
        if obs in self._observadores:
            self._observadores.remove(obs)

    def notificar_observadores(self, mensagem: str):
        for obs in self._observadores:
            obs.atualizar(mensagem)



class Ingresso(Sujeito, ABC):
    def __init__(self, nome: str, preco_base: float):
        super().__init__()
        self._nome = nome
        self._preco_base = preco_base

    @property
    def preco_base(self) -> float:
        return self._preco_base

    @preco_base.setter
    def preco_base(self, novo_preco: float):
        if novo_preco != self._preco_base:
            preco_antigo = self._preco_base
            self._preco_base = novo_preco
            mensagem = f"Notificação de Preço O preço do ingresso '{self._nome}' mudou de R$ {preco_antigo:.2f} para R$ {self._preco_base:.2f}."
            self.notificar_observadores(mensagem)

    @abstractmethod
    def calcular_preco_final(self, tipo_desconto: str = None, qtd: int = 1) -> float:
        pass


class CadeiraPremium(Ingresso):
    def __init__(self, preco_base: float):
        super().__init__("Cadeira Premium", preco_base)

    def calcular_preco_final(self, tipo_desconto: str = None, qtd: int = 1) -> float:
        return self._preco_base * qtd


class Arquibancada(Ingresso):
    def __init__(self, preco_base: float):
        super().__init__("Arquibancada", preco_base)

    def calcular_preco_final(self, tipo_desconto: str = None, qtd: int = 1) -> float:
        return self._preco_base * qtd


class Camarote(Ingresso):
    def __init__(self, preco_base: float):
        super().__init__("Camarote", preco_base)

    def calcular_preco_final(self, tipo_desconto: str = None, qtd: int = 1) -> float:
        return self._preco_base * qtd



class GerenciadorDescontos(Sujeito):
    def __init__(self):
        super().__init__()
        self._descontos_disponiveis = []

    def adicionar_desconto(self, nome_desconto: str, percentual: float):
        self._descontos_disponiveis.append({"nome": nome_desconto, "valor": percentual})
        mensagem = f"Novo Desconto Disponível Promoção lançada: '{nome_desconto}' ({percentual * 100:.0f}% de desconto)!"
        self.notificar_observadores(mensagem)



class Cliente(Observer):
    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, mensagem: str):
        print(f"-> Cliente: {self.nome} recebeu alerta: {mensagem}")


class Administrador(Observer):
    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, mensagem: str):
        print(f"==> Admin: {self.nome} registro no sistema: {mensagem}")



if __name__ == "__main__":
    print("--- 1. Inicializando Sistema e Atores ---")
    cliente1 = Cliente("Carlos Silva")
    cliente2 = Cliente("Ana Souza")
    admin1 = Administrador("Lucas (Gestor de Vendas)")
    ingresso_arquibancada = Arquibancada(preco_base=100.00)
    ingresso_camarote = Camarote(preco_base=350.00)
    sistema_descontos = GerenciadorDescontos()

    print("\n--- 2. Cadastrando Observadores nos Ingressos e Descontos ---")

    ingresso_arquibancada.adicionar_observador(cliente1)
    ingresso_arquibancada.adicionar_observador(cliente2)
    ingresso_arquibancada.adicionar_observador(admin1)
    sistema_descontos.adicionar_observador(cliente1)
    sistema_descontos.adicionar_observador(admin1)

    print("\n--- 3. Simulando Mudança de Preço no Ingresso de Arquibancada ---")

    ingresso_arquibancada.preco_base = 120.00

    print("\n--- 4. Simulando Adição de Novo Desconto ---")

    sistema_descontos.adicionar_desconto("Desconto de Estudante 50%", 0.50)
    sistema_descontos.adicionar_desconto("Pacote Família (Compre 4 Leve Mais)", 0.15)