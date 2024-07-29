import tkinter as tk
from tkinter import PhotoImage, StringVar, END, ANCHOR, BOTH, LEFT, RIGHT, BOTTOM

# Основное окно
root = tk.Tk()
root.title('To-Do List')
root.geometry("400x650+400+100")
root.resizable(False, False)

# Список задач
task_list = []

# Функция для удаления задачи
def deleteTask():
    global task_list
    task = listbox.get(ANCHOR)
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)

# Функция для добавления задачи
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(task + "\n")
        task_list.append(task)
        listbox.insert(END, task)

# Функция для открытия файла задач
def openTaskFile():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip():
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        open("tasklist.txt", "w").close()  # Создаем файл, если он не существует

# Установка иконки окна
image_icon = PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/task.png")
root.iconphoto(False, image_icon)

# Верхнее изображение
top_image = PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/topbar.png")
tk.Label(root, image=top_image).pack()

# Нижнее изображение
dock_image = PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/dock.png")
tk.Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

# Изображение заметки
note_image = PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/task.png")
tk.Label(root, image=note_image, bg="#32405b").place(x=340, y=25)

# Заголовок
heading = tk.Label(root, text="ALL TASKS", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Фрейм для ввода задачи
frame = tk.Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

# Поле ввода задачи
task = StringVar()
task_entry = tk.Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# Кнопка для добавления задачи
button = tk.Button(frame, text="Add", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# Фрейм для списка задач
frame1 = tk.Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

# Список задач
listbox = tk.Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

# Полоса прокрутки
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Открытие файла задач при запуске программы
openTaskFile()

# Кнопка для удаления задачи
delete_icon = PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/delete.png")
tk.Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
