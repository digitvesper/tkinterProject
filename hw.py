import tkinter as tk
import os

def add_task():
    task = task_entry.get()
    if task:
        task_list_box.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        task_list_box.delete(selected_task)

def mark_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        task_list_box.itemconfig(selected_task, bg="slate blue")

root = tk.Tk()
root.title("Task list")
root.configure(background="cornflower blue")
root.iconbitmap('1484271199-list_77857.ico')
root.geometry('400x600')
root.resizable(width = False, height = False)

path = os.path.abspath(os.curdir) +'\logo.png'
print(f"{path}")
Logo = tk.PhotoImage(file = path)
label = tk.Label(image = Logo, anchor = "c")
label.place(width = 400, relx =.5, anchor = "n")



text1 = tk.Label(root, text="Новая задача:",bg="cornflower blue")
text1.pack(pady = 1)

task_entry = tk.Entry(root, width = 38, bg="AliceBlue")
task_entry.pack(pady=18)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

detete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
detete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="cornflower blue")
text2.pack(pady=5)

task_list_box = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_list_box.pack(pady=10)

root.mainloop()