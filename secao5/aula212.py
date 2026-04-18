# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.


class Class:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print("oi", args, kwargs)


def funcao(*args, **kwargs):
    print("hey", args, kwargs)


c1 = Class()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Class.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)
