# Introdução aos packages (pacotes) em Python
from sys import path

import aula29_package.modulo
from aula29_package import modulo
from aula29_package.modulo import *

# from aula29_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula29_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
