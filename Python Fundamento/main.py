from usuario import Usuario

continuar = 1
listar_usuarios = []

while continuar != 0:
    try:
        nome = input("Digite o seu nome: ")
        idade = int (input("Digite sua idade: "))
        sobrenome = input("Digite seu sobrenome: ")
        usuario = Usuario(nome, idade, sobrenome)
        listar_usuarios.append(usuario)

        if idade == 99:
            break
        if idade == 98:
            continue
        print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

        if usuario.idade <= 17:
            print(f"{usuario.nome} é adolescente")
        elif usuario.idade >= 18 and usuario.idade <= 50:
            print(f"{usuario.nome} é adulto")
        else:
            print(f"{usuario.nome} é idoso")
        continuar = int(input("Deseja continuar o cadastro? 0 - Sair & 1 - Continuar"))
    except ValueError:
        print("Você deve informar um número válido!")


else:
    print("Lista de Usuarios Cadastrado: ")

    for x in listar_usuarios:
        print(f"Nome completo: {x.nome} {x.sobrenome} - Idade {x.idade} ")

    print(" O loop entrou no else")