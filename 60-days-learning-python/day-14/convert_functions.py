def convert(feet_inches):
    remove_space = feet_inches.split()
    feet = float(remove_space[0])
    inches = float(remove_space[1])
    return {'feet': feet, 'inches': inches}
    # return feet, inches