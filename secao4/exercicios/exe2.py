def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadriplica = criar_multiplicador(4)

print(duplica(6))
print(duplica(5))
print(duplica(10))
