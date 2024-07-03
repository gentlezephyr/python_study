while True:
    date = input("Enter a date: ")
    mood = int(input("Rate your mood on a scale of 1-10: "))
    if mood > 10 or mood < 1:
        print("You should select a number between 1-10!")
        continue
    else:
        pass
    thoughts = input("Enter your thoughts: ")

    with open(f"journal/{date}.txt", "w") as file:
        file.write(str(mood) + "\n")
        file.write(thoughts.capitalize())

    print("Deu bom família")
    break
