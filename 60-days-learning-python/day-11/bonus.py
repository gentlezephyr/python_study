def get_average():
    with open('files/data.txt', 'r') as file_local:
        data = file_local.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    average_sum = sum(values) / len(values)
    return average_sum


average = get_average()
print(average)
