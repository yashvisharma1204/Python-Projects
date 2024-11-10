def get_todos():
 
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def append_todos(todo):
   
    with open('todos.txt', 'a') as file:
        file.write(todo)
    return todo

def write_todo(todo):
  
    with open('todos.txt', 'w') as file:
        file.writelines(todo)
