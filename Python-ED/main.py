from array import array
from vetores import vetor
from listas import lista_ligada

#vetor_inteiros = array ('b', [1, 2, 3])
#print(vetor_inteiros)
#print(vetor_inteiros)
#print(vetor_inteiros.index(2))


print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Lista Ligadas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:

    vetor_teste = vetor.Vetor(0)
    #Inserir elemento posição
    #vetor_teste.inserir_elemento_posicao(1, 0)
    #vetor_teste.inserir_elemento_posicao(2, 1)
    #vetor_teste.inserir_elemento_posicao(3, 2)
    #vetor_teste.inserir_elemento_posicao(4, 2)
    #vetor_teste.inserir_elemento_posicao(5, 2)

    #Inserir elemento no final
    #vetor_teste.inserir_elemento_final(1)
    #vetor_teste.inserir_elemento_final(2)
    #vetor_teste.inserir_elemento_final(3)
    #vetor_teste.inserir_elemento_final(4)
    #vetor_teste.inserir_elemento_final(5)
    #print(vetor_teste.listar_elemento(0))
    #print(vetor_teste.listar_elemento(1))
    #print(vetor_teste.listar_elemento(2))
    #print(vetor_teste.listar_elemento(3))
    #print(vetor_teste.listar_elemento(4))
    #print(vetor_teste.listar_elemento(5))

   # print(vetor_teste.tamanho_vetor())
    #print(vetor_teste)
    #print(vetor_teste.contem(8))
    #print(vetor_teste.indice(4))
    #vetor_teste.remover_elemento_indice(3)
    #print(vetor_teste)
    #vetor_teste.remover_elemento(5)
    #print(vetor_teste)

elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(2)
    lista_teste.inserir(3)
    print(lista_teste)
