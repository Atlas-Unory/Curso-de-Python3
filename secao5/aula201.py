# Introdução ao método __init__ (inicializador de atributos)
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("Luiz", "Maria")

print(p1.nome)
print(p1.sobrenome)
