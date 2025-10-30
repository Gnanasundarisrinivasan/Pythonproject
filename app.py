import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):   
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()   
        return tasks
    else:
        print("File not found!")      
        

def save_tasks(task_list):
    with open(TASKS_FILE, "w") as file:    
        for task in task_list:
            file.write(task + "\n")

def show_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks yet!")
    else:
        for i in range(len(task_list)):
            print(i+1, task_list[i])   
def add_task(task_list):
    task = input("Enter task: ")
    if task != "":
        task_list.append(task)
        save_tasks(tasks)  
        print("Empty task!")

def delete_task(task_list):
    show_tasks(task_list)
    index = int(input("Enter task number to delete: "))
    if index >= 0 and index <= len(task_list):   
        task_list.pop(index)                     
        save_tasks(task_list)
    else:
        print("Invalid number")

def main():
    tasks = load_tasks()
    while True:
        print("1. View\n2. Add\n3. Delete\n4. Exit")
        ch = input("Enter choice: ")

        if ch == 1:         
            show_tasks(tasks)
        elif ch == "2":
            add_task(tasks)
        elif ch == "3":
            delete_task(tasks)
        elif ch == "4":
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()
