# O ponto de vista do __main__ pode te confundir em módulos e pacotes Python

from aula29_package.modulo import fala_oi, soma_do_modulo

print(__name__)
fala_oi()
