"""
I learnt/remembered:
 - input("Text for user")
 - match (switch)
 - you can add | (or) in case statement
 - list.append()
 - break to exit the while
 - enumerate function make available not only the items but also the indexes of the list
"""

todos = []

while True:
    user_action = input("Do you want to add, show or exit?")
    match user_action:
        case 'add':
            todo = input("Enter to do: ")
            todos.append(todo.title())
        case 'show' | 'display':
            for index, element in enumerate(todos):
                print(f'{index + 1} : {element}')
        case 'edit':
            edit_todo = int(input("What number do you want to edit?"))
            new_todo = input("Enter new value: ")
            todos[edit_todo - 1] = new_todo
        case 'complete':
            complete_item = int(input("What number do you want to complete?"))
            completed_item = todos.pop(complete_item - 1)
            print(f'You rock! "{completed_item}" Task was completed!')
        case 'exit':
            break

