

import json

with open("questions.json", "r") as file:
    content = file.read()
    data = json.loads(content)
    for question in data:
        print(question['question_text'])
        for index, answer in enumerate(question['alternatives']):
            print(f'{index+1}.{answer}')
        user_choice = int(input("What is the correct answer?"))
        if user_choice == question['correct_answer']:
            print("Answer is correct!")
        else: print("Sorry, the answer is incorrect!")

