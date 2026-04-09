# __dict__ e vars para atributos de instância


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {"nome": "João", "idade": 34}
p1 = Pessoa(**dados)

""" p1 = Pessoa("João", 34)
p2 = Pessoa("Helena", 23)

print(p1.__dict__) """

print(vars(p1))
print(p1.nome)
