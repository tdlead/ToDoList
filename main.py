"""
I learnt/remembered:
 - input("Text for user")
 - match (switch)
 - you can add | (or) in case statement
 - list.append()
 - break to exit the while
 - enumerate function make available not only the items but also the indexes of the list
"""

file_name = 'todos.txt'


def read_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


def write_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)


def print_content(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, element in enumerate(lines):
            print(f'{index + 1} : {element.strip()}')


while True:
    user_action: str = input("Do you want to add, show or exit?")

    if user_action.startswith('add'):
        todo = user_action[4:].strip().title() + '\n'
        todos = read_file(file_name)
        todos.append(todo)
        write_file(file_name, todos)

    elif user_action.strip() == 'show':
        print_content(file_name)

    elif user_action.startswith('edit'):
        try:
            edit_todo = int(user_action[5:].strip()) - 1
            new_todo = input("Enter new value: ").title() + '\n'
            todos = read_file(file_name)
            todos[edit_todo] = new_todo
            write_file(file_name, todos)
        except ValueError:
            print('Your command is not valid. Try to introduce number instead of text. ')
            continue
        except IndexError:
            print('There is no such number in to do list ')
            continue

    elif user_action.startswith('complete'):
        try:
            complete_item = int(user_action[8:].strip())
            todos = read_file(file_name)
            completed_item = todos.pop(complete_item - 1)
            write_file(file_name, todos)
            print(f'You rock! "{completed_item.strip()}" Task was completed!')
        except IndexError:
            print('There is no such number in to do list ')
            continue

    elif user_action.startswith('exit'):
        break
