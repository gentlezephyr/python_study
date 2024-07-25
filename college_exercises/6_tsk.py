count = 4
notas = []

while count > 0:
    nota = int(input('Digite uma nota: '))
    notas.append(nota)
    count = count - 1
    soma = sum(notas)
    media = soma / len(notas)

print(media)