a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

which_number = int(input('Write a number to show the lower ones: '))
lower_numbers = []

for number in a:
    if number < which_number:
        lower_numbers.append(number)

print(lower_numbers)