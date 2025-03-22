salas = [
    ['maria', 'helena', 'joao'],
    ['feranndo', 'gabriel', 'henrique'],
    ['mateus', 'felipe', 'edu']
]

""" print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3]) """

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)