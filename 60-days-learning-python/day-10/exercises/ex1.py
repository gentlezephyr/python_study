try:
    total_value = int(input("Enter the total value: "))
    discount = int(input("Enter the discount: "))

    if total_value <= 0:
        print("Your total value cannot be zero or negative!")
    else:
        result = (discount / total_value) * 100
        print(f"{result}%")

except ValueError:
    print("You need to enter a number, Run the program again!")