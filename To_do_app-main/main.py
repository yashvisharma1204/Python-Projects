from functions import get_todos,append_todos,write_todo
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is,",now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'  
        append_todos(todo)   
    elif user_action.startswith('show'):
        todos = get_todos()
        for i, item in enumerate(todos):
            item = item.strip()
            print(f'{i+1}. {item}')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number -= 1
    
            todos = get_todos()

            print("Here are the existing todos:")
            for i, item in enumerate(todos, 1):
                print(f'{i}. {item}', end='')
            new_todo = input("\nEnter your new todo: ") + '\n'
            todos[number] = new_todo

            write_todo(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith('complete'):
        number = int(user_action[9:])
        try:
            todos = get_todos()
            to_remove = todos.pop(number - 1)
            write_todo(todos)
            print(f"Todo '{to_remove.strip()}' has been removed from the list.")
        except IndexError:
            print("The number is not valid")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Try again!")

print("Bye!")
