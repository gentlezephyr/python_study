width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

try:
    if width == height:
        exit("The area of the rectangle is equal to the width")
    area = width * height
    print(area)
except ValueError:
    print("The area of the rectangle is not a valid number")

