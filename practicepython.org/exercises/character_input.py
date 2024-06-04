# Simple version

import datetime
from datetime import datetime

print("Discover the year when you'll be 100 years old!")
name = str(input("Write your name here: "))
age = int(input("Write your age here: "))

year = datetime.now().year

actual_year = (year - age) + 100

print(f"Your name is {name} and you'll be 100 in {actual_year}")

# Há alguma maneira de calcular os meses pra se ter um ano mais exato?