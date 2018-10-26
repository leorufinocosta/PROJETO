class Filecontrol:
    def __init__(self):
        self.file = None

    def ler_arq(self):
        est = open('estoque.txt', 'r')
        lista = est.read()
        est.close()