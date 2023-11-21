from abc import ABC, abstractmethod

class Carro(ABC):
    @abstractmethod
    def realizar_operacao(self):
        pass

class CarroReal(Carro):
    def realizar_operacao(self):
        print("Realizando operação no carro")

class ProxyControleAcesso(Carro):
    def __init__(self, carro_real, usuario_autorizado):
        self.carro_real = carro_real
        self.usuario_autorizado = usuario_autorizado

    def realizar_operacao(self):
        if self.usuario_autorizado:
            self.carro_real.realizar_operacao()
        else:
            print("Acesso não autorizado. Operação não permitida.")

if __name__ == "__main__":
    carro_real = CarroReal()
    
    proxy = ProxyControleAcesso(carro_real, usuario_autorizado=True)
    
    proxy.realizar_operacao()

    proxy.usuario_autorizado = False
    proxy.realizar_operacao()
