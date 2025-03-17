numero_str = input('vou dobrar um numero')

try:
    nuemro_float = float(numero_str)
    print(f'o dobro de {numero_str} é {nuemro_float * 2}')
except:
    print('Isso não é um número')
