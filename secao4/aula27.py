# Como importar coisas do seu próprio módulo (ponto de vista do __main__)

# Finja que o arquivo aula97_m existe para o código ter sentido
# Conteúdo do arquivo aula97_m:
"""
print('Este módulo se chama', __name__)
variavel_modulo = 'Luiz'


def soma(x, y):
    return x + y
"""

# nos caminhos de sys.path

import aula97_m
from aula97_m import soma, variavel_modulo

print("Este módulo se chama", __name__)
# print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 3))
