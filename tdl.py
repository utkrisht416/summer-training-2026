import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task!= "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Window setup
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x450")

tk.Label(root, text="To-Do List", font=("Arial", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white", width=15).pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=12)
listbox.pack(pady=20)

load_tasks()

root.mainloop()