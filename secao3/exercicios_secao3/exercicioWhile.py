nome_string = 'Luiz Otavio'
indice = 0
novo_nome = ''
    #print(f'{nome_string[0:]: * ^ 11}')

while indice < len(nome_string):
    letra = nome_string[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(f'{novo_nome}*')