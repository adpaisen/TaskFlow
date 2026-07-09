import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{index}. {status} {task['title']}")

def add_task(tasks):
    title = input("\nEnter task: ")

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added!")

def complete_task(tasks):
    show_tasks(tasks)

    try:
        number = int(input("\nTask number to complete: "))

        tasks[number - 1]["completed"] = True

        save_tasks(tasks)
        print("Task completed!")

    except:
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)

    try:
        number = int(input("\nTask number to delete: "))

        tasks.pop(number - 1)

        save_tasks(tasks)
        print("Task deleted!")

    except:
        print("Invalid task number.")

def menu():
    tasks = load_tasks()

    while True:
        print("""
====== TaskFlow ======

1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit
""")

        choice = input("Choose option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

menu()
