# Initialize an empty list to store tasks
tasks = []

def add_task():
    """Function to add a task to the list."""
    task = input("Enter task <- ")
    tasks.append(task)
    print("Added :)")

def view_tasks():
    """Function to view all tasks in the list."""
    if len(tasks) == 0:
        print("No tasks")
    else:
        for task in tasks:
            print(task)

def delete_task():
    """Function to delete a task from the list."""
    if len(tasks) != 0:
        task_to_delete = input("Enter task to delete <- ")
        if task_to_delete not in tasks:
            print("No such task")
        else:
            tasks.remove(task_to_delete)
            print("--->Deleted! :)")
    else:
        print("List is empty")

# Greet the user
print("Welcome, this program is made to help you keep track of your tasks :)")

# Main program loop
while True:
    command = input("[To add task-> a :: To view tasks-> v :: To delete last task-> d :: To exit-> e ]--->").lower()

    if command == "e":
        print("Exiting program...")
        break
    elif command == "a":
        add_task()
    elif command == "v":
        view_tasks()
    elif command == "d":
        delete_task()
    else:
        print("Unknown command. Please try the commands I gave you :)")
