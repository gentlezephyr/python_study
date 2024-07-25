litros = float(input('Quantos litros deseja?'))
opcao = int(input('Digite 1 para gasolina, 2 para etanol e 3 para gasolina aditivada'))

match opcao:
    case 1:
        gasolina = litros * 5
        print('O valor será R$', gasolina)
    case 2:
        etanol = litros * 3.50
        print('O valor será R$', etanol)
    case 3:
        gasolina_aditi = litros * 6.99
        print('O valor será R$', gasolina_aditi)
    case _:
        print('Valor inválido')
