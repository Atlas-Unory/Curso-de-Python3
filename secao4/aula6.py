# aula de closure

def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


bomdia = saudacao('bom dia')
bomanoite = saudacao('boa noite')

for nome in ['maria', 'fernanda', 'gabriela', 'leticia']:
    print(bomdia(nome))
    print(bomanoite(nome))
