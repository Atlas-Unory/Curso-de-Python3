class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua


cliente1 = Cliente("maria")
cliente1.inserir_endereco("av brasil", 40)
cliente1.inserir_endereco("rua b", 21)

print(cliente1.enderecos[0].rua)
print(cliente1.enderecos[1].rua)
