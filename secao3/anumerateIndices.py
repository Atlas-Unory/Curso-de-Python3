"""
enumerate é um metodo para pegar indices de iteraveis
"""

lista = ['maria', 'joao', 'fernada']
lista.append('carla')

# lista_enumerada = enumerate(lista)


# 1 forma de listar os indices
#print(next(lista_enumerada))

#forma de convertar os dados de uma lista junto com enumerate
# o (start=) é opcional

# pode ser usado assim, mas ainda não é a forma correta de usar
lista_enumerada = list(enumerate(lista, start=1))


#segunda forma de listar os indices
""" for indice in lista_enumerada:
    print(indice) """

# forma correta de usar enumerate
for item in enumerate(list(lista_enumerada)):
    indice, nome = item
    print(item)