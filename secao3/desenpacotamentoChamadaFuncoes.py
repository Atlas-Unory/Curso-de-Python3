lista = ['maria', 'joao', 1, 4, 2, 'carro']
string = ['ABCD']

salas = [
    ['maria', 'helena', 'joao'],
    ['feranndo', 'gabriel', 'henrique'],
    ['mateus', 'felipe', 'edu']
]

print(*lista)
print(*string)
print(*salas, sep='\n')