contador = 0
grupo = []

while contador < 3:
    dicionario = {}

    nomes = input('Qual é o seu nome: ')
    dicionario['nome'] = nomes
    idades = int(input('Digite a sua idade: '))
    dicionario['idade'] = idades
    grupo.append(dicionario)
    contador = contador + 1

print('Este grupo de três pessoas são:')
for pessoa in grupo:
    print(f'Nome: {pessoa['nome']}, Idade: {pessoa['idade']}')