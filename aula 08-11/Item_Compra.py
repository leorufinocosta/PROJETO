class Item_Compra():
    # MEtodo Construtor
    def __init__(self, nome, qtde):
        self.nome = nome
        self.qtde = qtde

     # metodo que converte a classe em texto
    def to_string(self):
        return self.nome + ';' + str(self.qtde)

    # metodo para ternar o nome
    def get_nome(self):
        return self.nome

    # metodo para retornar quantidade
    def get_qtde(self):
        return self.qtde