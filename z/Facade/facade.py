"""FACADE (estrutural): interface simples para um subsistema complexo."""


class Amplificador:
    def ligar(self): print("Amplificador: ligado")
    def volume(self, n): print(f"Amplificador: volume {n}")
    def desligar(self): print("Amplificador: desligado")


class Projetor:
    def ligar(self): print("Projetor: ligado")
    def modo_widescreen(self): print("Projetor: modo widescreen")
    def desligar(self): print("Projetor: desligado")


class Luzes:
    def apagar(self): print("Luzes: apagadas")
    def acender(self): print("Luzes: acesas")


class Streaming:
    def abrir(self, filme): print(f"Streaming: reproduzindo '{filme}'")
    def parar(self): print("Streaming: parado")


class HomeTheaterFacade:
    """O cliente chama 2 métodos em vez de orquestrar 4 subsistemas."""

    def __init__(self) -> None:
        self._amp, self._proj = Amplificador(), Projetor()
        self._luzes, self._stream = Luzes(), Streaming()

    def assistir_filme(self, filme: str) -> None:
        print("== Preparando o filme ==")
        self._luzes.apagar()
        self._proj.ligar()
        self._proj.modo_widescreen()
        self._amp.ligar()
        self._amp.volume(12)
        self._stream.abrir(filme)

    def encerrar(self) -> None:
        print("== Encerrando ==")
        self._stream.parar()
        self._amp.desligar()
        self._proj.desligar()
        self._luzes.acender()


if __name__ == "__main__":
    home = HomeTheaterFacade()
    home.assistir_filme("Interestelar")
    home.encerrar()