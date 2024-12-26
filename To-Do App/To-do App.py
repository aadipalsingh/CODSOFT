#Task01:- To-Do List application(CodSoft)
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App(CodSoft)")
        self.root.geometry("600x500")

    
        self.tasks = []

        
        self.title_label = tk.Label(self.root, text="To-Do List App", font=("Helvetica", 16, "bold"), bg="#222323", fg="white")
        self.title_label.pack(fill=tk.X)

    
        self.add_task_frame = tk.Frame(self.root, bg="#525252", pady=10)
        self.add_task_frame.pack(fill=tk.X)

        self.task_entry = tk.Entry(self.add_task_frame, font=("Helvetica", 12), width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=5)

        self.add_button = tk.Button(self.add_task_frame, text="➕ ADD TASK", font=("Helvetica", 10, "bold"), bg="#5783db", fg="white", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        self.task_list_frame = tk.Frame(self.root, bg="#222323", pady=10)
        self.task_list_frame.pack(fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(self.task_list_frame, font=("Helvetica", 12), width=50, height=15, bg="#adacac", fg="#333333", bd=2, relief=tk.SUNKEN)
        self.task_listbox.grid(row=0, column=0, padx=10, pady=5)

        self.edit_button = tk.Button(self.task_list_frame, text="✏️ Update", font=("Helvetica", 10), bg="#a881af", fg="white", command=self.edit_task)
        self.edit_button.grid(row=1, column=2, sticky="e", padx=10, pady=5)

        self.delete_button = tk.Button(self.task_list_frame, text="❌ Delete", font=("Helvetica", 10), bg="#ED0800", fg="white", command=self.delete_task)
        self.delete_button.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.mark_done_button = tk.Button(self.task_list_frame, text="✔️ Mark as Done", font=("Helvetica", 10), bg="#33b249", fg="white", command=self.mark_done)
        self.mark_done_button.grid(row=1, column=0, sticky="e", padx=10, pady=5)

        self.save_button = tk.Button(self.task_list_frame, text="💾 Save Tasks", font=("Helvetica", 10), bg="#ffbd03", fg="black", command=self.save_tasks)
        self.save_button.grid(row=1, column=0, sticky="s", padx=10, pady=5)

        self.status_frame = tk.Frame(self.root, bg="#525252", pady=10)
        self.status_frame.pack(fill=tk.X)

        self.total_label = tk.Label(self.status_frame, text="Total Tasks: 0", font=("Helvetica", 10), bg="#f0f0f0")
        self.total_label.grid(row=0, column=0, padx=20, pady=5)

        self.completed_label = tk.Label(self.status_frame, text="Completed: 0", font=("Helvetica", 10), bg="#f0f0f0")
        self.completed_label.grid(row=0, column=1, padx=20, pady=5)

        self.incomplete_label = tk.Label(self.status_frame, text="Incomplete: 0", font=("Helvetica", 10), bg="#f0f0f0")
        self.incomplete_label.grid(row=0, column=2, padx=20, pady=5)

    def add_task(self):
        new_task = self.task_entry.get().strip()
        if not new_task:
            messagebox.showwarning("Empty Task", "Please enter a task.")
            return
        self.tasks.append({"task": new_task, "done": False})
        self.task_entry.delete(0, tk.END)
        self.update_task_listbox()
        self.update_status()

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("No Selection", "Please select a task to edit.")
            return

        current_task = self.tasks[selected_task_index[0]]
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")
        edit_window.geometry("400x150")
        
        edit_label = tk.Label(edit_window, text="Edit Task:", font=("Helvetica", 12),bg="#222323", fg="white")
        edit_label.pack(pady=5)
        
        task_entry = tk.Entry(edit_window, font=("Helvetica", 12), width=40)
        task_entry.insert(0, current_task["task"])
        task_entry.pack(pady=10)
        
        def save_edited_task():
            new_task = task_entry.get().strip()
            if not new_task:
                messagebox.showwarning("Empty Task", "Please enter a task.")
                return
            self.tasks[selected_task_index[0]]["task"] = new_task
            self.update_task_listbox()
            self.update_status()
            messagebox.showinfo("Task Updated", "The task has been updated successfully.")
            edit_window.destroy()
        
        save_button = tk.Button(edit_window, text="Save", font=("Helvetica", 10), bg="#4681f4", fg="white", command=save_edited_task)
        save_button.pack(pady=10)
        
        edit_window.grab_set()  

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return

        task_to_delete = self.tasks[selected_task_index[0]]
        confirmation = messagebox.askyesno("Delete Task", f"Are you sure you want to delete the task: \n\"{task_to_delete['task']}\"?")
        if confirmation:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
            self.update_status()
            messagebox.showinfo("Task Deleted", "The task has been deleted successfully.")

    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("No Selection", "Please select a task to mark as done.")
            return

        self.tasks[selected_task_index[0]]["done"] = True
        self.update_task_listbox()
        self.update_status()

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    status = "done" if task["done"] else "not done"
                    file.write(f"{task['task']}|{status}\n")
            messagebox.showinfo("Save Successful", "Tasks saved to tasks.txt")
        except Exception as e:
            messagebox.showerror("Save Error", f"Error saving tasks: {e}")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["task"]
            if task["done"]:
                task_text += " (Done)"
            self.task_listbox.insert(tk.END, task_text)

    def update_status(self):
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["done"])
        incomplete = total - completed

        self.total_label.config(text=f"Total Tasks: {total}")
        self.completed_label.config(text=f"Completed: {completed}")
        self.incomplete_label.config(text=f"Incomplete: {incomplete}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
#that is all 