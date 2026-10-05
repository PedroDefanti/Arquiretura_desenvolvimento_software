from abc import ABC, abstractmethod


class ComponenteProduto(ABC):
    @abstractmethod
    def obter_preco(self) -> float:
        pass

    @abstractmethod
    def obter_descricao(self) -> str:
        pass


class ProdutoBase(ComponenteProduto):
    def __init__(self, nome_produto: str, preco_base: float):
        self.nome_produto = nome_produto
        self.preco_base = preco_base

    def obter_preco(self) -> float:
        return self.preco_base

    def obter_descricao(self) -> str:
        return self.nome_produto


class DecoradorProduto(ComponenteProduto, ABC):
    def __init__(self, item_produto: ComponenteProduto):
        self._item_produto = item_produto

    def obter_preco(self) -> float:
        return self._item_produto.obter_preco()

    def obter_descricao(self) -> str:
        return self._item_produto.obter_descricao()


class DecoradorImposto(DecoradorProduto):
    def __init__(self, item_produto: ComponenteProduto, taxa_percentual: float):
        super().__init__(item_produto)
        self.taxa_percentual = taxa_percentual  

    def obter_preco(self) -> float:
        return super().obter_preco() * (1 + self.taxa_percentual)

    def obter_descricao(self) -> str:
        return f"{super().obter_descricao()} + Imposto ({self.taxa_percentual * 100}%)"


class DecoradorDescontoFixo(DecoradorProduto):
    def __init__(self, item_produto: ComponenteProduto, valor_desconto: float):
        super().__init__(item_produto)
        self.valor_desconto = valor_desconto

    def obter_preco(self) -> float:
        return max(0.0, super().obter_preco() - self.valor_desconto)

    def obter_descricao(self) -> str:
        return f"{super().obter_descricao()} - Desconto (R${self.valor_desconto:.2f})"


class DecoradorPromocao(DecoradorProduto):
    def __init__(self, item_produto: ComponenteProduto, desconto_promocional: float):
        super().__init__(item_produto)
        self.desconto_promocional = desconto_promocional 

    def obter_preco(self) -> float:
        return super().obter_preco() * (1 - self.desconto_promocional)

    def obter_descricao(self) -> str:
        return f"{super().obter_descricao()} [Promo: {self.desconto_promocional * 100}% off]"


if __name__ == "__main__":
    
    computador = ProdutoBase("Notebook Gamer", 4000.00)
    print(f"Descrição: {computador.obter_descricao()} | Preço Base: R${computador.obter_preco():.2f}")
    
    computador_com_imposto = DecoradorImposto(computador, 0.10)
    
    computador_com_desconto = DecoradorDescontoFixo(computador_com_imposto, 200.00)
    
    computador_final = DecoradorPromocao(computador_com_desconto, 0.15)

    print("\n--- Resultado com Decorators aplicados em cadeia ---")
    print(f"Descrição Completa: {computador_final.obter_descricao()}")
    print(f"Preço Final Calculado: R${computador_final.obter_preco():.2f}")