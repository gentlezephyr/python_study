message = "Enter a password: "

password = input(message)

while password != "pass123":
    password = input("Enter a password: ")
    
print("The password is correct!")