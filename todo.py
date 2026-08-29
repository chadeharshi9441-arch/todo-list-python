tasks = []  # this will store our to-do items

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"'{task}' added to your list!")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"'{removed}' removed!")
            else:
                print("Invalid task number.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, try again.")