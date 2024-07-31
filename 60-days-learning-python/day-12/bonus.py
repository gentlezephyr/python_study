enter_feet_inches = input('Enter feet and inches: ')


def calc_feet_inches(enter_feet_inches):
    remove_space = enter_feet_inches.split()
    feet = float(remove_space[0])
    inches = float(remove_space[1])
    meters = feet * 0.3048 + inches * 0.0254
    meters = round(meters, 2)
    return meters


result = calc_feet_inches(enter_feet_inches)

if result < 1:
    print("Kid's too small")
else:
    print("Go ahead")
