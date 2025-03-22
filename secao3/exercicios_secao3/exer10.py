import os
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]serir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except TypeError:
            print('Não foi possivel apagar esté indice')
        except ValueError:
            print('Não foi possivel apagar esté indice')
        except IndexError:
            print('Não foi possivel apagar esté indice')

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Por favor, escolha i, a ou l')