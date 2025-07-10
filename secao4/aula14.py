# intance() para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

# exemplo 1
for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    # exemplo 2
    elif isinstance(item, str):
        print('str')
        print(item.upper())

    # exemplo 3
    elif isinstance(item, (int, float)):
        print("Num")
        print(item, item * 2)

    else:
        print("OUTRO")
        print(item)
