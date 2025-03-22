# import decimal
# O comando "import decimal" usa um módulo python chamado decimal, e dentro dele tem um método
# chamado Decimal(), ele não será usado em 99% das vezes. O Decimal() é usando apenas em casos que a precisão numérica é extrema,
# sendo geralmente usado em programas com finalidades científicas.

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2

print(numero3)
print(f'{numero3:.2f}')
print(round(numero3, 2))