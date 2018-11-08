from tkinter import *
from tkinter import messagebox
from Segunda_Janela import Segunda_Janela
# Classe Janela principal

class Janela_Principal(Tk):
    #Metodo construtor
    def __init__(self):
        #Executar o metodo da classe mae
        super().__init__()
        #Ajustar o tamanho
        self.geometry('300x300+200+200')
        #Colocar um titulo na janela
        self.title('Janela Principal')

        #Widgets na tela
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text="Ok", command=self.btn_ok_click)
        self.lbl_ok = Label(self, text='Teste')
        self.txt_ok = Entry(self)

        #Posicionando os widgets
        self.btn_close.place(x=10, y=250)
        self.btn_ok.place(x=140, y=250)
        self.lbl_ok.place(x=140, y=200)
        self.txt_ok.place(x=140, y=150)

        # == Menu ==
        #Criando um menu
        self.menu = Menu(self)
        #Criando um item de menu e subitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Segunda Janela', command=self.criar_segunda_janela)
        self.menu_principal.add_command(label='Comando 2')
        self.menu_principal.add_command(label='Comando 3')
        self.menu_principal.separator()
        self.menu_principal.add_command(label='sair', command=self.destroy)
        self.menu.add_cascade(label='Principal', menu=self.menu_principal)

        #Mostrando o mnenu
        self.config(menu=self.menu)

    # Metodo para fechar janela
    def destroy(self):
        # Janela de confirmação
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()

    # Metodo para o btn_ok
    def btn_ok_click(self):
        # mudar o texto de lbl_ok
        self.lbl_ok['text'] = self.txt_ok.get()

    # metodo para clicar no icone do menu
    def menu_click(self):
        messagebox.showinfo('Menu', 'Clicou no item de menu')

    #Metodo para criar a segunda janela
    def criar_segunda_janela(self):
        Segunda_Janela(self)