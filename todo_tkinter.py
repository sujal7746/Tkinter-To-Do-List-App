import tkinter as tk
from tkinter import messagebox

#create the main window
window = tk.Tk()
window.title("To-do List")
window.geometry("400x400")

tasks= []

def add_task():
    task_text = entry.get()
    if task_text:
        tasks.append({"title": task_text, "completed": False})
        update_task_list()
        entry.delete(0,tk.END)  #clear the entry box
    else:
        messagebox.showwarning("warning", "please enter a task")
    
def delete_task():
    selected = task_list.curselection()
    if selected:
        tasks.pop(selected[0])
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")


def toggle_task():
    selected = task_list.curselection()
    if selected():
        index = selected[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        update_task_list()
    else:
        messagebox.showwarning("warning", "please select a task to toggle")
    

def update_task_list():
    task_list.delete(0, tk.END)

    for task in tasks:
        display_text = f"[✓] {task['title']}" if task["completed"] else f"[ ] {task['title']}"
        task_list.insert(tk.END, display_text)


#create widgets
label = tk.Label(window, text="enter a task", font=("Arial",12))
label.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_list = tk.Listbox(window, height=15, width=50)
task_list.pack(pady=10)

toggle_button = tk.Button(window, text="Toggle Complete", command=toggle_task)
toggle_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

update_button = tk.Button(window, text="Update Task", command=update_task_list)
update_button.pack(pady=5)

window.mainloop()