#exercio dos nomes
""" nome_usuario = input('Digite seu nome: ')

if len(nome_usuario) < 4:
    print('Seu nome é curto')
elif (len(nome_usuario) >= 5) and (len(nome_usuario) < 6):
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')  """

#exercicio dos numeros impars
numero_digitado = input('Digite um núemro: ')
if numero_digitado.isdigit():
    print('é um número')

    numero_digitado = int(numero_digitado)
    n_impar = numero_digitado % 2 == 0
    n_impar_resultado = 'impar'

    if n_impar:
        n_impar_resultado = 'par'
    print(f'O numero {numero_digitado} é {n_impar_resultado}')
else:
    print('Você não digitou um número inteiro')