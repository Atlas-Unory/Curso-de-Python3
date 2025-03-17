""" frase = 'python dentro de frases pyton' \
        'muito python para ver aqui' """

frase = 'aaaooo'

i = 0
qtd_aparece_mais = 0
letra_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    qtd_atual= frase.count(letra_atual)


    if qtd_aparece_mais < qtd_atual:
        qtd_aparece_mais = qtd_atual
        letra_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi '
      f'"{letra_vezes}" que apareceu '
      f'{qtd_aparece_mais}x')