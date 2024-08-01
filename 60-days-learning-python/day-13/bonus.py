feet_inches = input('Enter feet and inches: ')


def convert(feet_inches):
    remove_space = feet_inches.split()
    feet = float(remove_space[0])
    inches = float(remove_space[1])
    return {'feet': feet, 'inches': inches}
    # return feet, inches


def calc(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    meters = round(meters, 2)
    return meters


parsed = convert(feet_inches)
result = calc(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet, {parsed['inches']} inches, result: {result}")

if result < 1:
    print("Kid's too small")
else:
    print("Go ahead")
