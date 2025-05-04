# metodos uteis para python

pessoa = {
    'nome': "luiz",
    'sobrenome': "miranda"
}

# print(len(pessoa))

# print(pessoa.keys())

# print(tuple(pessoa.values()))

print(tuple(pessoa.items()))

for chave, valor in pessoa.items():
    print(chave, valor)
