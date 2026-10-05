from abc import ABC, abstractmethod
from typing import List


class ComponenteSistema(ABC):
    @abstractmethod
    def exibir_informacoes(self, nivel_recuo: int = 0) -> None:
        pass

    @abstractmethod
    def obter_tamanho(self) -> int:
        pass


class ArquivoIndividual(ComponenteSistema):
    def __init__(self, titulo: str, tamanho_kb: int, dados: str):
        self.titulo = titulo
        self.tamanho_kb = tamanho_kb
        self.dados = dados

    def exibir_informacoes(self, nivel_recuo: int = 0) -> None:
        espacamento = "  " * nivel_recuo
        print(f"{espacamento}- [Arquivo] Nome: {self.titulo} | Tamanho: {self.tamanho_kb}KB | Conteúdo: {self.dados}")

    def obter_tamanho(self) -> int:
        return self.tamanho_kb


class Diretorio(ComponenteSistema):
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.elementos: List[ComponenteSistema] = []

    def adicionar_elemento(self, item: ComponenteSistema) -> None:
        self.elementos.append(item)

    def remover_elemento(self, item: ComponenteSistema) -> None:
        self.elementos.remove(item)

    def obter_tamanho(self) -> int:
        return sum(item.obter_tamanho() for item in self.elementos)

    def exibir_informacoes(self, nivel_recuo: int = 0) -> None:
        espacamento = "  " * nivel_recuo
        tamanho_total = self.obter_tamanho()
        print(f"{espacamento}+ [Pasta] Nome: {self.titulo} | Tamanho Total: {tamanho_total}KB")
        for item in self.elementos:
            item.exibir_informacoes(nivel_recuo + 1)

if __name__ == "__main__":
    diretorio_principal = Diretorio("Raiz")
    
    pasta_documentos = Diretorio("Documentos")
    pasta_documentos.adicionar_elemento(ArquivoIndividual("curriculo.pdf", 120, "Currículo profissional"))
    pasta_documentos.adicionar_elemento(ArquivoIndividual("compras.txt", 15, "Lista de mercado"))
    
    pasta_imagens = Diretorio("Imagens")
    pasta_imagens.adicionar_elemento(ArquivoIndividual("viagem.jpg", 2048, "[Dados da Imagem]"))
    
    diretorio_principal.adicionar_elemento(pasta_documentos)
    diretorio_principal.adicionar_elemento(pasta_imagens)
    diretorio_principal.adicionar_elemento(ArquivoIndividual("leia_me.md", 5, " Instruções"))
    
    print("--- Estrutura do Sistema de Arquivos ---")
    diretorio_principal.exibir_informacoes()