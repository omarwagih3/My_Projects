import time
tasks =[]
#start program greeting user
print("Welcome , this program is made to help you keep tracking of your tasks :)")

while True:
    #talking command from user
    command = input("[To add task-> a ::To view tasks-> v ::To delete last task-> d ::To exit-> e ]--->").lower()

    #checking command user entered

    #escape from program
    if command == "e":
        print("Exiting program...")
        for i in range(8):
            print("."*i)
            time.sleep(0.19)
        print("---->Done! :)")
        break

    #adding task to list
    elif command == "a":
        task =input("Enter task <- ")
        tasks.append(task)
        print("Added :)")

    #Viewing tasks
    elif command == "v":
        if len(tasks) == 0:
            print("No tasks")
        for task in tasks:
            print(f"{task}")

    #deleting a task from list
    elif command == "d":
        if len(tasks) != 0:
            task_to_delete = input("Enter task to delete <- ")
            if task_to_delete not in task:
                print("No such task")
            else:   
                tasks.remove(task_to_delete)
                print("--->Deleted! :)")
        else:        
            print("list is empty")

    else:
        print("unknown command please try commands i gave you :)")

