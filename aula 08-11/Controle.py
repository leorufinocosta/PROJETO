# importando
from Janela_Principal import Janela_Principal
from BD_Simulado import BD_Simulado
#classe controle
class Controle():
    # metodo construtor
    def __init__(self):
        # atributos
        self.bd = BD_Simulado()
        self.jnl = Janela_Principal(self)
        self.jnl.mainloop()

    # metodo para retornar lista de compras
    def get_lista_compras(self):
        return self.bd.get_lista_compras()