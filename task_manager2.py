#=====importing libraries===========
from datetime import datetime, date
#global variables
user_list = []
user_dict = {}
user_task = {}
task_percentage = {}
task_completed_percentage = {}
task_incompleted_percentage = {}
task_overdue = {}
#====defining functions====
# function to register a new user
def reg_user():
    
    username = input("Enter username: ")
    with open("user.txt", "r") as users:
        user_read = users.readlines()
    # error handling to ensure username has not been appended
    
    for line in user_read:
        split_data = line.strip("\n").split(", ")
        if username in line:
            print("This username has already been appended!")

    password = input("Enter password: ")
    confirmed_password = input("Please reenter password: ")

    if password == confirmed_password:
        with open("user.txt", "a") as users:
            users.write(f"{username}, {password}\n")

# function to add a task
def add_task():

    with open("tasks.txt", "a") as tasks:
                task_user = input("Please enter the username of the person the task is assigned to: ")
                task_title = input("Please enter the task title: ")
                task_description = input("Please enter a description of the task: ")
                task_duedate =input("Please enter the due date of the task (dd-mm-yyyy): ")
                current_date = input("Please enter the date the task was assigned (dd-mm-yyyy): ")
                tasks.write(f"{task_user}, {task_title}, {task_description}, {current_date}, {task_duedate}, No")

def view_all():

    with open("tasks.txt", "r") as tasks:
    # we display all tasks in the file

        for pos, line in enumerate(tasks, 1):
            split_line = line.split(", ")
            
            output = f"-------{[pos]}-------\n"
            output += "\n"
            output += f"Assigned to: {split_line[0]}\n"
            output += f"Task: {split_line[1]}\n"
            output += f"Description: {split_line[2]}\n"
            output += f"Assigned date: {split_line[3]}\n"
            output += f"Due date: {split_line[4]}\n"
            output += f"Is completed: {split_line[-1]}\n"
            output += "\n---------------\n"

            print(output)

def view_mine():

    with open("tasks.txt", "r") as tasks:
        tasks_read = tasks.readlines()
        # use a conditional statement to display the task of the user logged in
        for pos, line in enumerate(tasks_read, 1):
            split_line = line.split(", ")
            if user_name == split_line[0]:

                output = f"-------[{pos}]-------\n"
                output += "\n"
                output += f"Assigned to: {split_line[0]}\n"
                output += f"Task: {split_line[1]}\n"
                output += f"Description: {split_line[2]}\n"
                output += f"Assigned date: {split_line[3]}\n"
                output += f"Due date: {split_line[4]}\n"
                output += f"Is completed: {split_line[5]}\n"
                output += "\n---------------\n"

                print(output)
    
        while True: 
            choice = int(input("Select a task number or press -1 to return to the main menu: ")) -1

            if choice == -2:
                break

            edit_data = tasks_read[choice]
                

            choice_2 = int(input("""Select an option:
            1. Mark as completed
            2. Edit task """))
            
            # error handling
            if choice_2 < 1 or choice_2 > 2:
                print("Invalid option!")
                
            # we edit the text file to show task completed
            if choice_2 == 1:
                split_data = edit_data.split(", ")
                split_data[-1] = "Yes\n"
                new_data = ", ".join(split_data)
                tasks_read[choice] = new_data
                with open("tasks.txt", "w") as task_write:
                    for line in tasks_read:
                        task_write.write(line)
            
            # we edit the duedate and username of the task
            else:
                split_data = edit_data.split(", ")

            # error handling to make sure the task that is selected has not yet been completed
                if split_data[-1] == "yes\n":
                    print("You cant edit this task as it has been completed!")

                else:
                    split_data[0] = input("Please enter the username of who the task is assigned to: ")
                    split_data[-2] = input("Please enter due date of the task in the form dd-mm-yyyy: ")
                new_data = ", ".join(split_data)
                tasks_read[choice] = new_data

                with open("tasks.txt", "w") as task_write:
                    for line in tasks_read:
                        task_write.write(line)

# function to generate report
def gen_reports():

    # use the data from the original text files to create reports and write them to 2 new text files
    with open("tasks.txt", "r") as tasks:

        task_read = tasks.readlines()
        total_num_of_tasks = len(task_read)
        tasks_completed = 0
        tasks_uncompleted = 0
        tasks_overdue = 0
        for line in task_read:
            split_data = line.strip("\n").split(", ")
            date_today = datetime.today()
            split_data[-2] = datetime.strptime(split_data[-2], "%d-%b-%Y")
            # adding 1 to the variable for every completed task
            if split_data[-1] == "Yes":
                tasks_completed += 1

            # adding 1 to the variable for each incomplete task   
            if split_data[-1] == "No":
                tasks_uncompleted += 1

            # adding 1 to the variable for each overdue task
            if split_data[-2] > date_today and split_data[-1] == "No":
                tasks_overdue += 1

    # using simple maths to work out the percentage of tasks incopleted or overdue
    percentage_incomplete = round(((tasks_uncompleted/total_num_of_tasks)*100), 2)
    percentage_overdue = round(((tasks_overdue/total_num_of_tasks)*100), 2)

    # writing the information generated to a new text file 
    with open("task_overview.txt", "w+") as file:
        file.write(f"""\tThe total number of tasks: {total_num_of_tasks} 
        The total number of tasks completed: {tasks_completed}
        The total number of tasks incompleted: {tasks_uncompleted} 
        The total number of tasks overdue: {tasks_overdue}
        The percentage of tasks incomplete: {percentage_incomplete}% 
        The percentage of tasks overdue: {percentage_overdue}%""")

    with open("user.txt", "r") as users:
        user_read = users.readlines()
        total_num_of_users = len(user_read)
        for line in user_read:
            split_data = line.strip("\n").split(", ")
            # start by creating a list of all the users
            user_list.append(split_data[0])
            # creating dictionary for each piece of data with the key the username and value 0
            user_task[split_data[0]] = 0
            task_percentage[split_data[0]] = 0
            task_completed_percentage[split_data[0]] = 0
            task_incompleted_percentage[split_data[0]] = 0
            task_overdue[split_data[0]] = 0
    
    for user in user_list:
        total_tasks = 0
        completed_tasks = 0
        incomplete_tasks = 0
        overdue_tasks = 0
        with open("tasks.txt", "r") as tasks:
            tasks_read = tasks.readlines()
            for line in task_read:
                split_data2 = line.strip("\n").split(", ")
                split_data2[-2] = datetime.strptime(split_data2[-2], "%d-%b-%Y")

                # working out num of tasks
                if split_data2[0] == user:
                        total_tasks += 1

                # working out num of tasks completed 
                if split_data2[0] == user and split_data2[-1] == "Yes":
                    completed_tasks += 1
                    
                # working out tasks incompleted 
                if split_data2[0] == user and split_data2[-1] == "No":
                    incomplete_tasks += 1
                
                # working out overdue tasks 
                if split_data2[0] == user and split_data2[-1] == "No" and split_data2[-2] < date_today:
                    overdue_tasks +=1
        

        #adding this information to a dictionary
        while True:
            try:
                user_task[user] = total_tasks
                task_completed_percentage[user] = ((completed_tasks/ user_task[user])*100)
                task_incompleted_percentage[user] = ((incomplete_tasks / user_task[user])*100)
                task_overdue[user] = ((overdue_tasks / user_task[user])*100)
                break
            except ZeroDivisionError:
                return 0
        
    

        # working out percentage of tasks assigned to each user            
        for k in user_task:
            if k in task_percentage:
                task_percentage[k] = round((user_task[k]/total_num_of_tasks * 100), 2)

        # printing all data generated to text file in user friendly manner            
        output = ""
        for user in user_list:
            output += "=======================\n"
            output += f"{user}'s metrics\n"
            output += f"Total number of tasks assigned to {user}: {user_task[user]}\n"
            output += f"Total percentage of tasks assigned to {user}: {task_percentage[user]}%\n"
            output += f"Total percentage of completed tasks: {task_completed_percentage[user]}%\n"
            output += f"Total percentage of incompleted tasks: {task_incompleted_percentage[user]}%\n"
            output += f"Total percentage of overdue tasks: {task_overdue[user]}%\n\n"
        
        with open("user_overview.txt", "w+") as user_overview:
            user_overview.write(f"""The total number of tasks: {total_num_of_tasks} | The total number of users: {total_num_of_users}   
        {output}""")
                    
#====Login Section====
with open("user.txt", "r") as users:
    # forming a dictionary of names and passwords
    user_lines = users.readlines()
    for line in user_lines:
        key, value = line.strip("\n").split(", ")
        user_dict[key] = value
    print(user_dict)
while True:
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    # checking if an incorrect username or password was entered by using the get function in a dictionary

    if user_dict.get(user_name) == "None" or user_dict.get(user_name) != password:
        print("Invalid username or password, try again.")
        continue

    if user_dict[user_name] == password:
        print(f"Welcome {user_name}")
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
            add_task()

        elif menu == "va":
            view_all()
        
        elif menu == "vm":
            view_mine()
        
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
        ds - Display statistics
        gr - generate reports
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

        if menu == "r":
            reg_user()
        
        elif menu == "gr":
            gen_reports()
        
        elif menu == "ds":
            # in case we havnt generated reports we will first call the generate report function
            gen_reports()
            
            # displays statistics from the generate reports text files
            with open("task_overview.txt", "r") as file:
                for line in file:
                    print(line)
            
            with open("user_overview.txt", "r") as file:
                for line in file:
                    print(line)
        
        elif menu == "a":
            add_task()

        elif menu == "va":
            view_all()
        
        elif menu == "vm":
            view_mine()
        
        elif menu == "e":
            print("Good-bye!")
            break

        else:
            print("You have selected an invalid option, try again.")
            continue