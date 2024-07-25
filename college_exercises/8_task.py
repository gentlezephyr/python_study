genero = int(input('Digite 1 para homem ou 2 para mulher: '))

match genero:
    case 1:
        altura = float(input('Digite a sua altura: '))
        calculo = (72.7 * altura) - 58
        calculo_reduzido = round(calculo, 2)
    case 2:
        altura = float(input('Digite a sua altura: '))
        calculo = (62.1*altura) - 44.7
        calculo_reduzido = round(calculo, 2)
    case _:
        print('Valor inválido!')


print(calculo_reduzido)
