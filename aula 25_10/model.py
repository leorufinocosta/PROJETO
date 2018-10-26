#classe modelo
class Model:
    def __init__(self):
        self.lista_compras = {'Omo': 1, 'Arroz': 2, 'Bombril': 10}

    #Metodo de recuperação
    def get_lista_compras(self):
        return self.lista_compras