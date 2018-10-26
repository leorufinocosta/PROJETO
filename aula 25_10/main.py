from view import View
from control import Control
from model import Model

m = Model()

v = View()

c = Control(v, m)
#guardando a controller na view
v.set_control(c)

c.exibir_menu()