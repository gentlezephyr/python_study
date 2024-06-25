ips = ['100.122.133.105', '100.122.133.111']

for ip in ips:
    askIndex = int(input("Enter the index of the IP you want: "))
    askIndex -= 1
    ips[askIndex] = print(f'You chose: {ip}')
