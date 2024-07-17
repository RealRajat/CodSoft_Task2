import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.task_number = 1

        self.task_listbox = tk.Listbox(self.root, width=40)
        self.task_listbox.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        self.done_button = tk.Button(self.root, text="Mark task as done", command=self.mark_done)
        self.done_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_listbox.insert(self.task_number, task)
            self.task_number += 1
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        except IndexError:
            messagebox.showerror("Error", "Select a task to delete.")

    def mark_done(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks[task_index]["done"] = True
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, f"{self.tasks[task_index]['task']} *")
        except IndexError:
            messagebox.showerror("Error", "Select a task to mark as done.")

def main():
    root = tk.Tk()
    root.title("To-Do List")
    todo = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()