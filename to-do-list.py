import tkinter as tk
from tkinter import messagebox

class todolist:
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.tasks = []
        self.label=tk.Label(root, text="To-Do List",bg="yellow",fg="black",width=200,relief="sunken",font="'arial',16")
        self.label.pack()
        self.task_entry = tk.Entry(root,width=50,font="'arial',10")
        self.task_entry.pack(pady=10)
        self.add_button = tk.Button(root, text="Add Task", command=self.add,bg="Orange",fg="White")
        self.add_button.pack()
        self.task_listbox = tk.Listbox(root,selectmode=tk.SINGLE,width=50,font="'arial',10")
        self.task_listbox.pack(pady=10)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete,bg="#ff2e2e",fg="White")
        self.delete_button.pack()

    def add(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error!", "Please enter a task.")

    def delete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Error!", "Please select a task to delete.")

if __name__=="__main__":
    root = tk.Tk()
    app = todolist(root)
    root.resizable(0,0)
    root.geometry("280x350")
    root.mainloop()
