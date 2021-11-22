import abc,interface_veiculo

class Veiculo(interface_veiculo.InterfaceVeiculo, abc.ABC):
    """Essa é a classe carro. Esta classe é utilizada para indicarnovos carros em nosso programa"""
    def __init__(self, cor, tipo_combustivel, potencia, ):
        self.__cor = cor
        self.__tipo_combustivelipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = qtd_combustivel = 0
        self.__is_ligado = is_ligado = False
        self.__velocidade = velocidade = 0

    def __del__(self):
        print("O objeto foi removido da memoria. :")

    @property
    def cor (self):
        return self.__cor


    def abastecer(self, qtd_combustivel):
        self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            print(" O veiculo já está ligado")
        else:
            self.__is_ligado = True

    def desligar(self):
        if not self.__is_ligado == False:
            print(" O veiculo já esta desligado")
        else:
            self.is_ligado = False

    def acelerar(self, velocidade=10):
        if self.__is_ligado:
         self.__velocidade += velocidade
        else:
            print("O veiculo precisa estar ligado para acelerado")
