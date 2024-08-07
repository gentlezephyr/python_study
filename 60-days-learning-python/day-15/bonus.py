import json

with open('questions.json', 'r') as jsonfile:
    content = jsonfile.read()

data = json.loads(content)

score = 0
for question in data:
    print(question['item'])
    for index, options in enumerate(question['options']):
        print(index + 1, '-', options)
    answer = int(input('Write the answer here: '))
    question['user_answer'] = answer
    if question['user_answer'] == question['answer']:
        print('Correct')
        score += 1
    else:
        print('Incorrect')

result = f'You got {score} right from {len(data)}'
print(result)
