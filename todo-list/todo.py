tasks = []

def main():
    print("To-Do List App")
    print("\n")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(input("Enter the task: "))
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            if tasks:
                try:
                    task_index = int(input("Enter the task number to remove: "))
                    remove_tasks(task_index)
                    print("Task Removed.")
                except(ValueError, IndexError):
                    print("Invalid task number.")
            else:
                print("List is empty. No task to remove.")
            
        elif choice == '4':
            print("Program Terminated")
            break
        else:
            print("Invalid Choice! Please choose a number between 1 and 4.")
        

def show_menu():    
        print("To-Do List Menu:")
        print("""
            1. Add a task
            2. View tasks
            3. Remove a task
            4. Exit
        """)

def add_task(task):
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_tasks(task_index):
    tasks.pop(task_index - 1)

main()