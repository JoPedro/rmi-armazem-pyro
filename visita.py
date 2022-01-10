import sys
import Pyro5.errors
from Pyro5.api import Proxy
from pessoa import Pessoa

sys.excepthook = Pyro5.errors.excepthook

armazem = Proxy("PYRONAME:example.armazem")

gracon = Pessoa("Gracon")
joaopedro = Pessoa("João Pedro")

gracon.visitar(armazem)
joaopedro.visitar(armazem)