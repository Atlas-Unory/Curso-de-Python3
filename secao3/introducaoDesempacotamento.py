"""
Introdução ao desempacotamento
"""

# lista = ['maria', 'helena', 'joao']
# apredendo a extrair valores de indices de listas em variaveis
""" nome1, nome2 = ['maria', 'helena', 'joao']

print(nome1) """

# usnado a variavel (*resto) para empacotar o restante da lista
""" nome1, *resto = ['maria', 'helena', 'joao']

print(nome1, resto) """

# usando a variavel (*_) pode-se ignorar o restante da lista e usar só a parte que desejar
_ ,nome2, *_ = ['maria', 'helena', 'joao']
print(nome2)