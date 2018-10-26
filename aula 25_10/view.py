class View:

    def __init__(self):
        self.control = None

    def set_control(self, control):
        self.control = control

    def exibir_menu(self):
        resposta = True
        while resposta:
            print('''
            1. Exibir lista
            2. Incluir item
            3. Excluir item
            4. Sair
            ''')

            # Solicitar opção
            resposta = input("Digite um número: ")

            if resposta == '1':
                print('\n Lista de itens')
                self.exibir_lista_compras(self.control.get_lista_compras())
            elif resposta == '2':
                self.incluir_item()
                print('\n Item incluido')
            elif resposta == '3':
                print('\n Item excluido')
            elif resposta == '4':
                print('\n Tchau!')
                resposta = False
            else:
                print('\n Valor incorreto')

    #Metodo para exibir lista de compras
    def exibir_lista_compras(self, lista_compras):
        # A lista de compras é um dicionario
        # Percorrer o dicionario
        for chave, valor in lista_compras.items():
            print(f'- {chave} : {valor}')

    def incluir_item(self):
        qual_item = input("Qual item quer adicionar: ")
        quantos = input("Qual a quantidade: ")