from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def iniciar_transporte(self):
        pass

    @abstractmethod
    def transportar_carga(self):
        pass

    @abstractmethod
    def encerrar_transporte(self):
        pass



class VeiculoRodoviario(Veiculo):
    
    def iniciar_transporte(self):
        print("Transporte rodoviário iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por rodovia.")

    def encerrar_transporte(self):
        print("Transporte rodoviário encerrado.")


class VeiculoFerroviario(Veiculo):

    def iniciar_transporte(self):
        print("Transporte ferroviário iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por ferrovia.")

    def encerrar_transporte(self):
        print("Transporte ferroviário encerrado.")


class VeiculoMaritimo(Veiculo):

    def iniciar_transporte(self):
        print("Transporte marítimo iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por via marítima.")

    def encerrar_transporte(self):
        print("Transporte marítimo encerrado.")


class VeiculoAereo(Veiculo):

    def iniciar_transporte(self):
        print("Transporte aéreo iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por via aérea.")

    def encerrar_transporte(self):
        print("Transporte aéreo encerrado.")



class Logistica(ABC):
    
    @abstractmethod
    def criar_veiculo(self):
        pass

    def realizar_transporte(self):

        veiculo = self.criar_veiculo()

        veiculo.iniciar_transporte()
        veiculo.transportar_carga()
        veiculo.encerrar_transporte()
        
        
        

class LogisticaRodoviaria(Logistica):
    
    def criar_veiculo(self):
        return VeiculoRodoviario()


class LogisticaFerroviaria(Logistica):

    def criar_veiculo(self):
        return VeiculoFerroviario()


class LogisticaMaritima(Logistica):

    def criar_veiculo(self):
        return VeiculoMaritimo()


class LogisticaAerea(Logistica):

    def criar_veiculo(self):
        return VeiculoAereo()



def main():
    
    rodoviaria = LogisticaRodoviaria()
    rodoviaria.realizar_transporte()

    print()

    ferroviaria = LogisticaFerroviaria()
    ferroviaria.realizar_transporte()

    print()

    maritima = LogisticaMaritima()
    maritima.realizar_transporte()

    print()

    aerea = LogisticaAerea()
    aerea.realizar_transporte()


if __name__ == "__main__":
    main()
