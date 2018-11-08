#Importando das bibliotecas
from tkinter import *
from tkinter import messagebox
#Classe Segunda Janela
class Segunda_Janela(Toplevel):
    # Metodo construtor
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('Segunda Janela')
        self.transient(parent)
        self.grab_set()
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy())
        #Posicionando os widgets
        self.btn_close.place(x=10, y=150)
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()