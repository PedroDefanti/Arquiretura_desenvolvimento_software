from abc import ABC, abstractmethod



class ElementoHTM_Base(ABC):
    @abstractmethod
    def renderizar(self):
        pass


class Paragrafo(ElementoHTM_Base):
    pass


class Tabela(ElementoHTM_Base):
    pass


class Imagem(ElementoHTM_Base):
    pass


class Link(ElementoHTM_Base):
    pass


class Formulario(ElementoHTM_Base):
    pass



class ParagrafoHTML5(Paragrafo):
    def __init__(self, texto):
        self.texto = texto

    def renderizar(self):
        return f"<p>{self.texto}</p>"


class TabelaHTML5(Tabela):
    def renderizar(self):
        return """<table>
    <tr>
        <th>Nome</th>
        <th>Idade</th>
    </tr>
    <tr>
        <td>João</td>
        <td>20</td>
    </tr>
</table>"""


class ImagemHTML5(Imagem):
    def __init__(self, url, texto_alternativo):
        self.url = url
        self.texto_alternativo = texto_alternativo

    def renderizar(self):
        return f'<img src="{self.url}" alt="{self.texto_alternativo}">'


class LinkHTML5(Link):
    def __init__(self, url, texto):
        self.url = url
        self.texto = texto

    def renderizar(self):
        return f'<a href="{self.url}">{self.texto}</a>'


class FormularioHTML5(Formulario):
    def renderizar(self):
        return """<form>
    <label>Nome:</label>
    <input type="text" name="nome">
    <button type="submit">Enviar</button>
</form>"""



class FabricaHTML_Base(ABC):
    @abstractmethod
    def criar_paragrafo(self):
        pass

    @abstractmethod
    def criar_tabela(self):
        pass

    @abstractmethod
    def criar_imagem(self):
        pass

    @abstractmethod
    def criar_link(self):
        pass

    @abstractmethod
    def criar_formulario(self):
        pass



class FabricaHTML5(FabricaHTML_Base):
    def criar_paragrafo(self):
        return ParagrafoHTML5("Este é um parágrafo HTML.")

    def criar_tabela(self):
        return TabelaHTML5()

    def criar_imagem(self):
        return ImagemHTML5("https://exemplo.com/imagem.jpg", "Imagem de exemplo")

    def criar_link(self):
        return LinkHTML5("https://www.google.com", "Acessar página")

    def criar_formulario(self):
        return FormularioHTML5()



def main():
    fabrica = FabricaHTML5()

    paragrafo = fabrica.criar_paragrafo()
    tabela = fabrica.criar_tabela()
    imagem = fabrica.criar_imagem()
    link = fabrica.criar_link()
    formulario = fabrica.criar_formulario()

    print(paragrafo.renderizar())
    print(tabela.renderizar())
    print(imagem.renderizar())
    print(link.renderizar())
    print(formulario.renderizar())


if __name__ == "__main__":
    main()