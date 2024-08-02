from convert_functions import convert
from parses_functions import calc

feet_inches = input('Enter feet and inches: ')


parsed = convert(feet_inches)
result = calc(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet, {parsed['inches']} inches, result: {result}")

if result < 1:
    print("Kid's too small")
else:
    print("Go ahead")
