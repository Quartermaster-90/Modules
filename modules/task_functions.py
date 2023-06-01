
# Functions to complete:
## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    return [task for task in list if task["time_taken"] >= time]

## Find a task with a given description
def get_task_with_description(list, description):
    return [task for task in list if task["description"] == description][0]
            
# Extention (Function): 
## Get a list of tasks by status
def get_tasks_by_status(list, status):
    return [task for task in list if task["completed"] == status]

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)



