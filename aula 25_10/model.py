#classe modelo
class Model:
    def __init__(self):
        self.lista_compras = open('estoque.txt', 'r')

    #Metodo de recuperação
    def get_lista_compras(self):
        return self.lista_compras