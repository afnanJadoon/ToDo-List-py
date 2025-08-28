import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entryBox.get()
    if task != "":
        task_number = listBox.size() + 1  
        formatted_task = f"{task_number}.   {task}"  
        listBox.insert(tk.END, formatted_task)
        entryBox.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
        
def delete_task():
    try:
        selected = listBox.curselection()[0]
        listBox.delete(selected)
        
        tasks = listBox.get(0, tk.END)
        listBox.delete(0, tk.END)
        for i, task in enumerate(tasks, start=1):
            task_text = task.split(".   ")[-1] 
            listBox.insert(tk.END, f"{i}.   {task_text}")
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")
window.configure(bg="lightblue")

label1 = tk.Label(window, text="To-Do List", font=("Arial", 16, "bold"), bg="lightblue")
label1.pack(pady=5)

frame = tk.Frame(window, bg="lightblue")
frame.pack(pady=10)

label2 = tk.Label(frame, text="Enter your task:", font=("Arial", 10), bg="lightblue")
label2.pack(side="left")

entryBox = tk.Entry(frame, width=25, bd=2, bg="white")
entryBox.pack(side="right")

listBox = tk.Listbox(window, width=35, height=18, bd=2, font=("Arial", 10))
listBox.pack(pady=10)

bottomFrame = tk.Frame(window, bg="lightblue")
bottomFrame.pack(side="bottom", pady=10)

addTask = tk.Button(bottomFrame, text="Add Task", font=("Arial", 10, "bold"), width=15, bg="white", command=add_task)
addTask.pack(side="left", padx=10)

deleteTask = tk.Button(bottomFrame, text="Delete Task", font=("Arial", 10, "bold"), width=15, bg="white", command=delete_task)
deleteTask.pack(side="right", padx=10)

window.mainloop()
