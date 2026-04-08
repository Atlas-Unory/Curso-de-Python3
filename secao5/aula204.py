# Escopo da classe e de métodos da classe


class Animal:
    def __init__(self, nome):
        self.nome = nome
        variavel = "valor"
        print(variavel)

    def comendo(self, alimento):
        return f"{self.nome} está commendo uma {alimento}"

    def executa(self, *args, **kwargs):
        return f"{self.comendo(*args, *kwargs)}"


leao = Animal(nome="leao")
print(leao.nome)
print(leao.comendo("maçã"))
print(leao.executa("carne"))
