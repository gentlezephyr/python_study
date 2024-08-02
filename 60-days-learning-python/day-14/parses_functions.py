def calc(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    meters = round(meters, 2)
    return meters