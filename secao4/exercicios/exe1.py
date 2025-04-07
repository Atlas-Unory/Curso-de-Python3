def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicar = multiplica(1, 2, 3, 4, 5)
print(multiplicar)


def parImpar(numero):
    mutliplo_de_dois = numero % 2
    if mutliplo_de_dois == 0:
        return f"{numero} é par"

    return f"{numero} é impar"


print(parImpar(2))
print(parImpar(3))
print(parImpar(4))
print(parImpar(5))
