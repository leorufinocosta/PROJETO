# Importando classe
from Item_Compra import Item_Compra

class BD_Simulado():
    # Metodo construtor
    def __init__(self):
        #Atibutos
        self.lista_compras = []
        self.carregar_lista_compras()

    # Metodo carregas lista de compras
    def carregar_lista_compras(self):
        # Colocar aqui código para abrir arquivo
        # Cada linha do arquivo separar nome e quantidade split(';')
        # Para cada linha do arquivo criar um objeto de item compra

        item1 = Item_Compra('tomate', 10)
        item2 = Item_Compra('banana', 5)
        item3 = Item_Compra('cafe', 1)
        self.lista_compras.append(item1)
        self.lista_compras.append(item2)
        self.lista_compras.append(item3)
        #  remover até aqui

    def gravar_lista_compra(self):
        # abrir o arquivo para gravação
        # PErcorrer a lista
        # Para cada item da lista converter string
        # salvar no arquivo
        # remover essa parte
        for item in self.lista_compras:
            print(item.to_string())
        # remover ate aqui
    # metodo para retornar o item compra de acordo com o nome
    def get_item_compra(self):
        # Percorrer a lista
        for item in self.lista_compras:
            # se o nome for igual
            if (item.get_nome() == nome):
                return item
        # se nao encontrar
        return None

    # Metodo para retornar lista de compras
    def get_lista_compras(self):
        return self.lista_compras