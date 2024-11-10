import tkinter as tk
from tkinter import ttk, messagebox
from functions import get_todos, append_todos, write_todo
from PIL import ImageTk, Image

def add_todo():
    todo_text = todo_entry.get("1.0", tk.END).strip()
    if todo_text:
        append_todos(todo_text + '\n')
        update_todos()
        todo_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a to-do item")

def update_todo():
    selected_index = todo_listbox.curselection()
    if selected_index:
        new_todo_text = todo_entry.get("1.0", tk.END).strip()
        if new_todo_text:
            todos = get_todos()
            index = selected_index[0]
            todos[index] = new_todo_text + '\n'
            write_todo(todos)
            update_todos()
        else:
            messagebox.showwarning("Warning", "Please enter a to-do item to update")
    else:
        messagebox.showwarning("Warning", "Please select a to-do item to update")

def complete_todo():
    selected_index = todo_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        todos = get_todos()
        completed_todo = todos.pop(index)
        write_todo(todos)
        update_todos()
        messagebox.showinfo("Completed", f"To-do item '{completed_todo.strip()}' has been completed.")
    else:
        messagebox.showwarning("Warning", "Please select a to-do item to complete")

def write_todos():
    todos = [todo.strip() + '\n' for todo in todo_listbox.get(0, tk.END)]
    write_todo(todos)

def update_todos():
    todos = get_todos()
    todo_listbox.delete(0, tk.END)
    for i, todo in enumerate(todos, 1):
        todo_listbox.insert(tk.END, f'{i}. {todo.strip()}')


root = tk.Tk()
root.title("To-Do App")
root.configure(bg="medium sea green")  

todo_entry = tk.Text(root, width=40, height=6)
todo_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

write_label = tk.Label(root, text="Write your new task", font=("Monospace", 15, "bold"), fg="white", bg="medium sea green")
write_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nw")

add_button = ttk.Button(root, text="Add Todo", command=add_todo, width=25, style="C.TButton")
add_button.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="ne")


update_button = ttk.Button(root, text="Update Todo", command=update_todo, width=25, style="C.TButton")
update_button.grid(row=1, column=1, padx=(0, 10), pady=40, sticky="ne")


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)


complete_button = ttk.Button(root, text="Complete", command=complete_todo, width=25, style="C.TButton")
complete_button.grid(row=1, column=1, padx=(0, 10), pady=70, sticky="ne")

to_do_label = tk.Label(root, text="To-do List", font=("Monospace", 20, "bold"), fg="white", bg="medium sea green")
to_do_label.grid(row=1, column=0, padx=10, pady=(120,0), sticky="nw")

todo_listbox = tk.Listbox(root, width=55,height=12)
todo_listbox.grid(row=2, column=0, rowspan=3, padx=10, pady=10, sticky="ns")

# Image in column 2
image_path = "31d0ad0f84c1c86e87dbcd62d09d51f1.jpg" 
img = Image.open(image_path)
img = img.resize((200,300))  
img = ImageTk.PhotoImage(img)
image_label = tk.Label(root, image=img, highlightthickness=0)
image_label.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")
update_todos()


style = ttk.Style()
style.configure("C.TButton", foreground="Green",background="medium sea green", borderwidth=0, font=("Monospace", 10, "bold"))

style.map("C.TButton", background=[('active', "medium sea green")], bordercolor=[('active', "#4f5f77")])

style = ttk.Style()
style.configure("C.TButton", foreground="Green",background="medium sea green", borderwidth=0, font=("Monospace", 10, "bold"))

style.map("C.TButton", background=[('active', "medium sea green")], bordercolor=[('active', "#4f5f77")])

root.mainloop()
