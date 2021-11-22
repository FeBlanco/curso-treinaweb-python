import  abc

class InterfaceVeiculo(abC.ABC):

    @abc.abstractmethod
    def cor(self, COR):
        pass

    @abc.abstractmethod
    def ligar(self):
        pass

    @abc.abstractmethod
    def abastecer(self, qtd_combustivel):
        pass

    @abc.abstractmethod
    def desligar(self):
        pass

    @abc.abstractmethod
    def acelerar(self, velocidade=10):
        pass