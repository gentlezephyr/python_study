num = int(input("Write a number here: "))
check = int(input("Write the divisible number here: "))

if check == 2:
    if num % 4 == 0:
        print("This number is a multiple of 4")
    elif num % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
else:
    print("Check doesn't divide equally")
    
# Descobrindo se um número é ímpar ou par através de condicionais e o operador modular.

# Esse exercício mostra bem a questão da ordem de precedência de um código. Apesar de que há maneiras de realizar duas veríficações
# em um código e torná-lo mais inteligente?