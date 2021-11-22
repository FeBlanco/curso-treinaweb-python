import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiro = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        print("O metodo foi chamado a partir da classe Moto: ")
        if self._qtd_combustivel >= 30:
          print("A moto está cheia")
        else:
          self._qtd_combustivel += qtd_combustivel