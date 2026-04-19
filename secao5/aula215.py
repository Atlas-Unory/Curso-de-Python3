# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯


class Caneta:

    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        """Essa funão, 'cor', é o getter"""
        print("PROPERTY")
        return self._cor

    @cor.setter
    def cor(self, valor):
        """Essa funão, 'cor', é o setter. O setter tem que ter o mesmo nome da função"""
        print("estou no setter", valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta("Verde")
caneta.cor = "amarela"
caneta.cor = "roxa"
caneta.cor_tampa = "lilas"

print(caneta.cor)
print(caneta.cor_tampa)
