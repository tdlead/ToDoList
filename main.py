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
    user_action = input("Do you want to add, show or exit?")

    match user_action:
        case 'add':
            todo = input("Enter to do: ")
            todo = todo.title() + '\n'

            todos = read_file(file_name)
            todos.append(todo)
            write_file(file_name, todos)

        case 'show' | 'display':
            print_content(file_name)

        case 'edit':
            edit_todo = int(input("What number do you want to edit?")) - 1
            new_todo = input("Enter new value: ").title() + '\n'
            todos = read_file(file_name)
            todos[edit_todo] = new_todo
            write_file(file_name, todos)

        case 'complete':
            complete_item = int(input("What number do you want to complete?"))
            todos = read_file(file_name)
            completed_item = todos.pop(complete_item - 1)
            write_file(file_name, todos)
            print(f'You rock! "{completed_item.strip()}" Task was completed!')
        case 'exit':
            break
