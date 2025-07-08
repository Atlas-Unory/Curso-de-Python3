# Introdução a list comprehension

lista = []

for numero in range(10):
    lista.append(numero)

lista = [numero for numero in range(10)]
print(lista)
