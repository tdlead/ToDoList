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
            edit_todo = input("What element do you want to edit?")
            new_todo = input("Enter new to do: ")
            index = todos.index(edit_todo)
            todos[index] = new_todo
        case 'exit':
            break
