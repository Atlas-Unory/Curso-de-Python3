# Métodos em instâncias de classes Python


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelera(self):
        print(f"{self.nome} está acelerando...")


fusca = Carro("Fusca")
fusca.acelera()

celta = Carro("Celta")
celta.acelera()
