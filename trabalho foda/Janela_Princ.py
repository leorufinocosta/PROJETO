from tkinter import *
from tkinter import messagebox

class Janela_Princ(Tk):
    def __init__(self, controle):
        #atributos
        self.controle = controle
        super().__init__()
        self.geometry('300x300+200+200')
        self.title('Concessionária')

        #Widgets na tela
        self.bt1 = Button(self, width=10, text='Uno')
        self.bt1.pack(padx= 0, pady=10)
        self.bt2 = Button(self, width=10, text='Mobi')
        self.bt2.pack(padx=0, pady=10)
        self.bt3 = Button(self, width=10, text='Sandero')
        self.bt3.pack(padx=0, pady=10)
        self.bt4 = Button(self, width=10, text='HB20')
        self.bt4.pack(padx=0, pady=10)
        self.bt5 = Button(self, width=10, text='Gol')
        self.bt5.pack(padx=0, pady=10)
        self.bt6 = Button(self, width=10, text='Palio')
        self.bt6.pack(padx=0, pady=10)

        self.menu = Menu(self)
        #Criando um item de menu e subitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Carros Disponíveis')
        self.menu_principal.add_command(label='Vendas')
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair', command=self.fechar)
        self.menu.add_cascade(label='Consultar', menu=self.menu_principal)

        #Mostrando o mnenu
        self.config(menu=self.menu)

    def fechar(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()