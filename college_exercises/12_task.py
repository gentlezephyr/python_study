horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
valor_hora = float(input('Digite o valor da hora trabalhada: '))

if valor_hora and horas_trabalhadas > 0:
    salario = valor_hora * horas_trabalhadas
    print(f'O seu salário é: {salario}')
