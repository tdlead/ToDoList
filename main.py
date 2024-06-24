"""
I learnt/remembered:
 - input("Text for user")
 - match (switch)
 - you can add | (or) in case statement
 - list.append()
 - break to exit the while
 - enumerate function make available not only the items but also the indexes of the list
"""

from modules import functions

FILEPATH = 'todos.txt'

while True:
    user_action: str = input("Do you want to add, show or exit?")

    if user_action.startswith('add'):
        todo = user_action[4:].strip().title() + '\n'
        todos = functions.read_file(FILEPATH)
        todos.append(todo)
        functions.write_file(FILEPATH, todos)

    elif user_action.strip() == 'show':
        functions.print_content(FILEPATH)

    elif user_action.startswith('edit'):
        try:
            edit_todo = int(user_action[5:].strip()) - 1
            new_todo = input("Enter new value: ").title() + '\n'
            todos = functions.read_file(FILEPATH)
            todos[edit_todo] = new_todo
            functions.write_file(FILEPATH, todos)
        except ValueError:
            print('Your command is not valid. Try to introduce number instead of text. ')
            continue
        except IndexError:
            print('There is no such number in to do list ')
            continue

    elif user_action.startswith('complete'):
        try:
            complete_item = int(user_action[8:].strip())
            todos = functions.read_file(FILEPATH)
            completed_item = todos.pop(complete_item - 1)
            functions.write_file(FILEPATH, todos)
            print(f'You rock! "{completed_item.strip()}" Task was completed!')
        except IndexError:
            print('There is no such number in to do list ')
            continue

    elif user_action.startswith('exit'):
        break
