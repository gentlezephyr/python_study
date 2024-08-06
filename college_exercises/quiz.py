perguntas = [
    {'item': 'Qual a função utilizada para exibir mensagens na tela em Python?', 'resposta': 'print'},
    {'item': 'Qual o operador utilizado para a multiplicação em Python?', 'resposta': '*'},
    {'item': 'Qual palavra-chave é usada para definir uma função em Python?', 'resposta': 'def'},
    {'item': 'Como você inicia um comentário em Python?', 'resposta': '#'},
    {'item': 'Qual função é usada para ler a entrada do usuário em Python?', 'resposta': 'input'}
]

pontuacao = 0

for item in perguntas:
    tentativas = 2
    while tentativas > 0:
        resposta = input(item['item'] + ' ')
        if resposta.lower() == item['resposta'].lower():
            if tentativas == 2:
                pontuacao += 10
            elif tentativas == 1:
                pontuacao += 5
            break
        else:
            tentativas -= 1

if pontuacao == 50:
    print(f'Excelente, sua pontuação foi {pontuacao}')
elif 37 < pontuacao < 49:
    print(f'Ótimo, sua pontuação foi {pontuacao}')
elif 25 < pontuacao < 36:
    print(f'Bom, sua pontuação foi {pontuacao}')
else:
    print(f'Ruim, sua pontuação foi {pontuacao}')
