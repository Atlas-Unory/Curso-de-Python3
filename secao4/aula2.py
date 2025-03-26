# Aula de argumentos nomeados e não nomeados

# os não nomeados devem ser enviados na ordem dos argumentos passados na declaração da função, neste caso soma()
# os argumentos nomedos podem der passados em qualquer ordem e eles não vão atrapalhar os parametros passados para a função
# pois eles estão nomeados
"""
Exemplo de argumentos não nomeados e nomeados:
def soma(x, y):
    print(x + y)

# Argumentos não nomeados:
soma(1, 2)

# Argumentos nomeados:
soma(x=1, y=2)

# mesmo que a ordem seja dos argumentos seja diferente do que está nos paramentos
# não via mudar o resultado final pois eles estão nomeados

OBS: todos os argumentos que vem apos um argumento nomedo, também devem ser nomeados ou dará um erro
OBS2: argumentos não nomeados são chamados de argumentos posicionais
"""

def soma(x, y):
    print(x + y)

# argumentos não nomeados:
soma(1, 2) # os não nomeados devem ser enviados na ordem dos argumentos passados na declaração da função, neste caso soma()