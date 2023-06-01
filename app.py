import modules.task_functions as task_functions
import modules.output as output
import modules.input as input
import data.task_list as task_list

while (True):
    output.print_menu()
    option = input.get_user_input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        output.print_list(task_list.tasks)
    elif option == '2':
        output.print_list(task_functions.get_tasks_by_status(task_list.tasks,False))
    elif option == '3':
        output.print_list(task_functions.get_tasks_by_status(task_list.tasks,True))
    elif option == '4':
        description = input.get_user_input("Enter task description to search for: ")
        task = task_functions.get_task_with_description(task_list.tasks, description)
        if task is not None:
            task_functions.mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = int(input.get_user_input("Enter task duration: "))
        output.print_list(task_functions.get_tasks_taking_at_least(task_list.tasks, time))
    elif option == '6':
        description = input.get_user_input("Enter task description to search for: ")
        print(task_functions.get_task_with_description(task_list.tasks, description))
    elif option == '7':
        description = input.get_user_input("Enter description: ")
        time_taken = int(input.get_user_input("Enter time taken: "))
        task = task_functions.create_task(description, time_taken)
        task_list.tasks.append(task)
    else:
        print("Invalid Input - choose another option")
