from .no import No

class ListaLigada():
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__tamanho = 0

        #INSERIR na lista
    def inserir(self, elemento):
        novo_no = No(elemento)
        if self.esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        self.__tamanho += 1
        #VERIFICAR SE ESTA VAZIO
    def esta_vazia(self):
        return self.__tamanho == 0

        #IMPRIMINDO NA LISTA

    def __str__ (self):
        temp = self.__primeiro_no
        elementos =''
        while (temp):
            elementos = f'{elementos} {temp.elemento}'
            temp = temp.proximo
        return elementos



