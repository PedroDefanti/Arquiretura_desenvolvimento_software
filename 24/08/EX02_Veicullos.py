from abc import ABC, abstractmethod


class Veiculo_base(ABC):

    @abstractmethod
    def iniciar_transporte(self):
        pass

    @abstractmethod
    def transportar_carga(self):
        pass

    @abstractmethod
    def encerrar_transporte(self):
        pass



class Veiculo_Da_Rodovia(Veiculo_base):
    
    def iniciar_transporte(self):
        print("Transporte rodoviário iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por rodovia.")

    def encerrar_transporte(self):
        print("Transporte rodoviário encerrado.")


class Veiculo_Da_Ferrovia(Veiculo_base):

    def iniciar_transporte(self):
        print("Transporte ferroviário iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por ferrovia.")

    def encerrar_transporte(self):
        print("Transporte ferroviário encerrado.")


class Veiculo_Da_Maritima(Veiculo_base):

    def iniciar_transporte(self):
        print("Transporte marítimo iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por via marítima.")

    def encerrar_transporte(self):
        print("Transporte marítimo encerrado.")


class Veiculo_Da_Aerea(Veiculo_base):

    def iniciar_transporte(self):
        print("Transporte aéreo iniciado.")

    def transportar_carga(self):
        print("Carga sendo transportada por via aérea.")

    def encerrar_transporte(self):
        print("Transporte aéreo encerrado.")



class Logistica_base(ABC):
    
    @abstractmethod
    def criar_veiculo(self):
        pass

    def realizar_transporte(self):

        veiculo = self.criar_veiculo()

        veiculo.iniciar_transporte()
        veiculo.transportar_carga()
        veiculo.encerrar_transporte()
        
        
        

class Logistica_Da_Rodoviaria(Logistica_base):
    
    def criar_veiculo(self):
        return Veiculo_Da_Rodovia()


class Logistica_Da_Ferroviaria(Logistica_base):

    def criar_veiculo(self):
        return Veiculo_Da_Ferrovia()


class Logistica_Da_Maritima(Logistica_base):

    def criar_veiculo(self):
        return Veiculo_Da_Maritima()


class Logistica_Da_Aerea(Logistica_base):

    def criar_veiculo(self):
        return Veiculo_Da_Aerea()



def main():
    
    rodoviaria = Logistica_Da_Rodoviaria()
    rodoviaria.realizar_transporte()

    print()

    ferroviaria = Logistica_Da_Ferroviaria()
    ferroviaria.realizar_transporte()

    print()

    maritima = Logistica_Da_Maritima()
    maritima.realizar_transporte()

    print()

    aerea = Logistica_Da_Aerea()
    aerea.realizar_transporte()


if __name__ == "__main__":
    main()
