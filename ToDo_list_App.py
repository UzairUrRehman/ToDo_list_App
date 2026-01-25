todo_list = []


def menu():
    while(True):
        print(f"*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")


        choice = int(input("Enter a Choice: "))
        print(f"\n")
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            complete_task()
        elif choice == 5:
            print("Exiting the Application . . . ")
            exit()
        else:
            print(f"Invalid Choice! Try Again!!!")


def add_task():
    task = input("Enter a Task: ")
    todo_list.append({"Task" : task, "Status" : "pending"})
    print(f"Task Added Successfully!\n")


def view_task():
    if len(todo_list) == 0:
        print("No Pending Tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print(f"\n")


def remove_task():
    if len(todo_list) == 0:
        print(f"List is Empty!\n")
    else:
        try:
            find_task = int(input("Enter the task number you want to find: "))
            find_task = find_task -1
            if 0 <= find_task < len(todo_list):
                removed_task = todo_list.pop(find_task)
                print(f"Task removed: {removed_task['Task']}\n")
            else:
                print(f"Invalid Task number!\n")
        except ValueError: 
            print(f"Please Enter a Valid Task Number!\n")
          

def complete_task():
    if len(todo_list) == 0:
        print(f"List is Empty!\n")
    else:
        try:
            find_task = int(input("Enter the task number you want to mark completed: "))
            find_task = find_task -1
            if 0 <= find_task < len(todo_list):
                todo_list[find_task]['Status'] = 'completed'
                print(f"Task {todo_list[find_task]['Task']} has been marked as Completed!\n")
            else:
                print(f"Invalid Task number!\n")
        except ValueError: 
            print(f"Please Enter a Valid Task Number!\n")

print(f"Welcome to ToDo List App!\n")
menu()