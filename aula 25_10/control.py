class Control:
    def __init__(self, view, model):
        self.view = view
        self.model = model

#metodo para exibir menu
    def exibir_menu(self):
        self.view.exibir_menu()

    def get_lista_compras(self):
        return self.model.get_lista_compras()

    #def incluir_item(self):
     #   if view.qual_item in model.lista_compras == True:


