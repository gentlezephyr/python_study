while True:
    asking_member = input("Add a new member: ")
    asking_member = asking_member

    file = open("members.txt", "r")
    members = file.readlines()
    file.close()

    members.append(f"{asking_member}\n")

    file = open("members.txt", "w")
    for member in members:
        file.write(member)
    file.close()
