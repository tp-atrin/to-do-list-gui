import tkinter as tk

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = tk.Listbox(self.master, width=40)
        self.tasks.pack(pady=10)

        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.master, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def edit_task(self):
        selected_task = self.tasks.curselection()
        if selected_task:
            task = self.tasks.get(selected_task)
            edit_window = tk.Toplevel(self.master)
            edit_window.title("Edit Task")

            edit_entry = tk.Entry(edit_window, width=30)
            edit_entry.pack(pady=10)
            edit_entry.insert(0, task)

            save_button = tk.Button(edit_window, text="Save", command=lambda: self.save_task(selected_task, edit_entry))
            save_button.pack(pady=5)

    def save_task(self, selected_task, edit_entry):
        new_task = edit_entry.get()
        self.tasks.delete(selected_task)
        self.tasks.insert(selected_task, new_task)
        edit_entry.delete(0, tk.END)
        edit_entry.insert(0, new_task)

    def remove_task(self):
        selected_task = self.tasks.curselection()
        if selected_task:
            self.tasks.delete(selected_task)

if __name__ == "__main__":
    root = tk.Tk()
    to_do_list = ToDoList(root)
    root.mainloop()
