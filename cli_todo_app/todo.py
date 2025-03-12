import click # to create a cli
import json # to save and load tasks from file
import os # to check if the file exists

TODO_FILE = "todo.json" #file where the data will be stored

def load_tasks(): #to load the existing data from the file
    if not os.path.exists(TODO_FILE): #to see if the file exist or not
        return [] #if not then return an empty list
    with open(TODO_FILE, "r") as file: #if exist then open the file in read mode
        return json.load(file) #load the data and returns it
        
def save_tasks(tasks): #to update the list
    with open(TODO_FILE, "w") as file: #open the file in write mode 
        json.dump(tasks, file, indent=4) #update the tasks in file and indent for better readability
        
@click.group() #create cli group which let us define multiple commands
def cli():  #main cli group, returns nothing
    """Simple Todo List Manager"""
    pass

@click.command() #create command to add task in the list
@click.argument("task") #create argument to put task in the list through command
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task":task, "done":False}) #task is incompleted (by default)
    save_tasks(tasks)
    click.echo(f'Task added successfully: {task}') #print on the cli
  
@click.command() #create command for list preview
def lst(): 
    tasks = load_tasks()
    if not tasks:
        click.echo("No task found!")
        return
    for index, task in enumerate(tasks, 1): #loop through the tasks while giving index to each task starting from 1
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} [{status}]")
    
@click.command() #create command to mark the task as completed
@click.argument("task_number", type=int) #create argument to define the task number which is to be marked as done
def complete(task_number):
    """Mark task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True 
        save_tasks(tasks)
        click.echo(f"task {task_number} marked as completed")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command() #create command to remove the task from the list
@click.argument("task_number", type=int) #create the argument to define the task number which is to be removed
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo(f"Invalid task number: {task_number}")

#registration of commands under CLI group       
cli.add_command(add)
cli.add_command(lst)
cli.add_command(complete)
cli.add_command(remove)

#to run the cli after the execution of script or file
if __name__ == "__main__":
    cli()
    
    
