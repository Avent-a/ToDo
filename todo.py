import tkinter 
from tkinter import *

root = Tk()
root.title('todo')
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open ("tasklist.txt", 'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        
        listbox.delete(ANCHOR)

def addTask():
    task = task_entery.get()
    task_entery.delete(0,END)

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END,task)

def openTaskFile():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task.strip():
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        open("tasklist.txt", "w").close()  # Create the file if it does not exist

Image_icon=PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/task.png")
root.iconphoto(False,Image_icon)

topImage=PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/topbar.png")
Label(root,image=topImage).pack()

dockImage=PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/dock.png")
Label(root,image=dockImage, bg="#32405b").place(x=30,y=25)

noteImage=PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/task.png")
Label(root, image=noteImage,bg="#32405b").place(x=340,y=25)

heading=Label(root,text="ALL TASK", font="arial 20 bold", fg="white",bg="#32405b")
heading.place(x=130,y=20)

frame = Frame(root, width=400, height=50, bg ="white")
frame.place(x=0, y=180)

task=StringVar()
task_entery=Entry(frame, width=18, font="arial 20", bd=0)
task_entery.place(x=10, y=7)
task_entery.focus()

button=Button(frame,text="add", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2) 
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

Delete_icon=PhotoImage(file="/home/alex/Документы/ToDo List/photo todo/delete.png")
Button(root,image=Delete_icon,bd=0, command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()
