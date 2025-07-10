# Dictionary comprehension e set comprehension

produto = {
    "nome": "caneta",
    "preco": 1.20,
    "categoria": "escritorio"
}

# exemplo 1
dc = {
    chave: valor
    for chave, valor
    in produto.items()
}

# exemplo 2
dc1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

# exemplo 3
dc2 = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
}

# exemplo 4

lista = [
    ('a', 'brics a'),
    ('b', 'brics a'),
    ('c', 'brics a'),
]

dc3 = {
    chave: valor
    for chave, valor in lista
}


# exemplo 5
# set comprehension
dc4 = {i ** 3 for i in range(10)}

print(dc4)
