# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.


class Pessoa:
    ano = 2030

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("hey")

    @classmethod
    def cria_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("anonima", idade)


p1 = Pessoa("joão", 30)
print(Pessoa.ano)
p2 = Pessoa.cria_com_50_anos("mateus")
p3 = Pessoa.criar_sem_nome(20)
print(p3.nome, p3.idade)
print(p2.nome, p2.idade)
