#=====importing libraries===========
from datetime import date
#====Login Section====
with open("user.txt", "r") as users:
    # forming 2 seperate lists to store the name and password
    user_lines = users.readlines()
    list_user_names = []
    list_password = []
    for line in user_lines:
        split_data = line.split(", ")
        list_user_names.append(split_data[0].strip())
        list_password.append(split_data[-1].strip("\n"))
    
while True:
    user_name = input("please enter a username: ")
    password = input("Please enter a password: ")
    # a check to find out if the name and password are in the user text file
    check_1 = list_user_names.count(user_name)
    check_2 = list_password.count(password)
    if check_1 <= 0 or check_2 <= 0:
        print("You have entered an incorrect username or password, please try again.")
        continue

    elif user_name in list_user_names and list_password[list_user_names.index(user_name)] != password:
        print("You have entered an incorrect username or password, please try again.")
        continue

    elif password in list_password and list_user_names[list_password.index(password)] != user_name:
        print("You have entered an incorrect username or password, please try again.")
        continue

    if user_name in list_user_names and list_password[list_user_names.index(user_name)] == password:
        break
    
while True:
    if user_name != "admin":
        # we use a conditional statement to display the menu to all users aside for the admin
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()
        if menu == "a":
            # this writes a new task to the task file
            with open("tasks.txt", "a") as tasks:
                task_user = input("Please enter the username of the person the task is assigned to: ")
                task_title = input("Please enter the task title: ")
                task_description = input("Please enter a description of the task: ")
                task_duedate =input("Please enter the due date of the task: ")
                current_date = input("Please enter the date the task was assigned: ")
                tasks.write(f"\n{task_user}, {task_title}, {task_description}, {current_date}, {task_duedate}, No")
                
        elif menu == "va":
            with open("tasks.txt", "r") as tasks:
                # we display all tasks in the file

                for line in tasks:
                    split_line = line.split(", ")
                    
                    output = "--------------\n"
                    output += "\n"
                    output += f"Assigned to: {split_line[0]}\n"
                    output += f"Task: {split_line[1]}\n"
                    output += f"Description: {split_line[2]}\n"
                    output += f"Assigned date: {split_line[3]}\n"
                    output += f"Due date: {split_line[4]}\n"
                    output += f"Is completed: {split_line[5]}\n"
                    output += "\n---------------\n"

                    print(output)
                    
        elif menu == "vm":
            with open("tasks.txt", "r") as tasks:
                # use a conditional statement to display the task of the user logged in
                
                for line in tasks:
                    split_line = line.split(", ")
                    if user_name == split_line[0]:

                        output = "---------------\n"
                        output += "\n"
                        output += f"Assigned to: {split_line[0]}\n"
                        output += f"Task: {split_line[1]}\n"
                        output += f"Description: {split_line[2]}\n"
                        output += f"Assigned date: {split_line[3]}\n"
                        output += f"Due date: {split_line[4]}\n"
                        output += f"Is completed: {split_line[5]}\n"
                        output += "\n---------------\n"

                        print(output)
                        
        elif menu == "e":
            print("Good-bye!")
            break

        else:
            print("You have selected an invalid option, try again.")
            continue

    else:
        # the admin has an extra 2 options
        menu = input('''Select one of the following Options below:
        r - Registering a user
        d - Display statistics
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()
        if menu == "r":
            # we register a user and append to user text file
            with open("user.txt", "a") as users:
                user_name2 = input("Please enter a username: ")
                password2 = input("Please enter a password: ")
                confirmed_password = input("Please reenter your password: ")
                if confirmed_password == password2:
                    users.write(f"{user_name2}, {password2}\n")
                else:
                    print("Your passwords don't match, sorry!")
            
        elif menu == "d":
            # we display the statistics of how many tasks and users there are using a for loop
            with open("user.txt", "r") as users:
                count = 0
                for line in users:
                    count += 1
                print(f"The amount of users is {count}")
            with open("tasks.txt", "r") as tasks:
                count = 0
                for line in tasks:
                    count += 1
                print(f"The amount of tasks is {count}")
        
        elif menu == "a":
            # this writes a new task to the task file
            with open("tasks.txt", "a") as tasks:
                task_user = input("Please enter the username of the person the task is assigned to: ")
                task_title = input("Please enter the task title: ")
                task_description = input("Please enter a description of the task: ")
                task_duedate =input("Please enter the due date of the task: ")
                current_date = input("Please enter the date the task was assigned: ")
                tasks.write(f"\n{task_user}, {task_title}, {task_description}, {current_date}, {task_duedate}, No")
                
        elif menu == "va":
            with open("tasks.txt", "r") as tasks:
                # we display all tasks in the file

                for line in tasks:
                    split_line = line.split(", ")
                    
                    output = "--------------\n"
                    output += "\n"
                    output += f"Assigned to: {split_line[0]}\n"
                    output += f"Task: {split_line[1]}\n"
                    output += f"Description: {split_line[2]}\n"
                    output += f"Assigned date: {split_line[3]}\n"
                    output += f"Due date: {split_line[4]}\n"
                    output += f"Is completed: {split_line[5]}\n"
                    output += "\n---------------\n"

                    print(output)
                    
        elif menu == "vm":
            with open("tasks.txt", "r") as tasks:
                # use a conditional statement to display the task of the user logged in
                
                for line in tasks:
                    split_line = line.split(", ")
                    if user_name == split_line[0]:

                        output = "---------------\n"
                        output += "\n"
                        output += f"Assigned to: {split_line[0]}\n"
                        output += f"Task: {split_line[1]}\n"
                        output += f"Description: {split_line[2]}\n"
                        output += f"Assigned date: {split_line[3]}\n"
                        output += f"Due date: {split_line[4]}\n"
                        output += f"Is completed: {split_line[5]}\n"
                        output += "\n---------------\n"

                        print(output)
                        
        elif menu == "e":
            print("Good-bye!")
            break

        else:
            print("You have selected an invalid option, try again.")
            continue
