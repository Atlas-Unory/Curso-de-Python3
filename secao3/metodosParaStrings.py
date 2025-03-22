frase = 'olha só, que coisa legal'

lista_palavras_crua = frase.split(',')

print(lista_palavras_crua)

lista_frase = []
for i, frase in enumerate(lista_palavras_crua):
    lista_frase.append(lista_palavras_crua[i].strip())

print(lista_palavras_crua)
print(lista_frase)

frase_unida = '-'.join(lista_frase)
print(frase_unida)

frase1 = 'camelo amarelo'

frase2 = frase1.split(sep=' ')

print(frase2)