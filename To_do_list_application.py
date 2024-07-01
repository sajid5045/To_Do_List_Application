import tkinter as tk
from tkinter import messagebox

# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "Done" if task["completed"] else "Not Done"
        listbox_tasks.insert(tk.END, f"{task['task']} ({status})")

# Function to add a task to the to-do list
def add_task():
    task_name = entry_task.get()
    if task_name:
        task = {"task": task_name, "completed": False}
        tasks.append(task)
        entry_task.delete(0, tk.END)
        display_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        tasks[selected_task_index]["completed"] = True
        display_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to remove a task from the to-do list
def remove_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        tasks.pop(selected_task_index)
        display_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Main window setup
window = tk.Tk()
window.title("To-Do List")

# Create GUI elements
frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(window, width=50)
entry_task.pack()

button_add_task = tk.Button(window, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_mark_completed = tk.Button(window, text="Mark as completed", width=48, command=mark_completed)
button_mark_completed.pack()

button_remove_task = tk.Button(window, text="Remove task", width=48, command=remove_task)
button_remove_task.pack()

button_quit = tk.Button(window, text="Quit", width=48, command=window.quit)
button_quit.pack()

# Start the main loop
window.mainloop()
