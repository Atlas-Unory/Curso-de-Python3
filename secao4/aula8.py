# Empacotamento de desempacotamendo de dicionarios

pessoa = {
    "nome": "Aline",
    "sobrenome": "Moreira"
}

(a1, a2), (b1, b2) = pessoa.items()

print(a1, b1)
print(a2, b2)

dados_pessoa = {
    "idade": 24,
    "altura": 2.32
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)
