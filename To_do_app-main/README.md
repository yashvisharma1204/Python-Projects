# 📝 To-Do App

A simple to-do application with a graphical user interface (GUI) built using `tkinter`. This app allows you to add, update, and complete tasks. The tasks are stored in a text file (`todos.txt`), so your to-do list persists between sessions.

## Features

- ➕ Add new to-do items
- ✏️ Update existing to-do items
- ✅ Mark to-do items as completed
- 📋 List and view all to-do items

## File Structure

- `main.py` and `gui.py`: Main application code including the GUI and user interactions.
- `functions.py`: Helper functions for reading, writing, and updating the to-do list stored in `todos.txt`.
- `todos.txt`: Text file to store the to-do items.

## `functions.py`

Contains the following functions:

- `get_todos()`: Reads the `todos.txt` file and returns a list of to-do items.
- `append_todos(todo)`: Appends a new to-do item to the end of the `todos.txt` file.
- `write_todo()`: Writes a list of to-do items to the `todos.txt` file, replacing its contents.

## `main.py` and `gui.py`

Main application logic including the GUI setup and user interaction functions.

### GUI Setup

The GUI is created using `tkinter`. It includes a main window, text entry for to-dos, listbox to display to-dos, and buttons for various actions.

### Button Functions

- `add_todo()`: Adds a new to-do item and updates the listbox.
- `update_todo()`: Updates the selected to-do item.
- `complete_todo()`: Marks a to-do item as completed by removing it from the list.
- `write_todos()`: Writes the current state of the listbox to the `todos.txt` file.
- `update_todos()`: Updates the listbox with the current to-do items.

### Run the Application

The application is run using `tkinter`'s `mainloop()` function.

## Screenshots
<img width="432" alt="image" src="https://github.com/yashvisharma1204/To_do_app/assets/137611141/d26db249-ddde-42f4-8572-62c5311c46c5">

### Write and ADD using add button
<img width="435" alt="image" src="https://github.com/yashvisharma1204/To_do_app/assets/137611141/5369086d-d568-46ad-a234-11190d53db9f">

### Update the already added task by update todo
!!! Select the todo first<br>
<img width="435" alt="image" src="https://github.com/yashvisharma1204/To_do_app/assets/137611141/42a4a3ee-8379-4022-a518-6b1335678b63">

### Complete a task and remove it from list
<img width="435" alt="image" src="https://github.com/yashvisharma1204/To_do_app/assets/137611141/edb6321b-1724-45dd-9cdf-a75ab65ff865">
