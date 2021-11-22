import carro, moto, veiculo

uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
uno_vermelho.pintar("azul")
print(f"A quantidade de combustivel do carro é:")

if isinstance( (uno_vermelho, veiculo.Veiculo)):
    print("A classe é veiculo")

else:
    print("A classe não é veiculo")


