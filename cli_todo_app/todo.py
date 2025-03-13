import click # to create a cli
import json # to save and load tasks from file
import os # to check if the file exists

TODO_FILE = "todo.json" #file where the data will be stored

# Function to load tasks from the file 
def load_tasks(): 
    """Loads existing tasks from the JSON file.  
    If the file does not exist, returns an empty list."""  
    if not os.path.exists(TODO_FILE): # Check if the file exists
        return [] #if not, return an empty list
    
    with open(TODO_FILE, "r") as file: # Open the file in read mode 
        return json.load(file) # Load JSON data and return it as a Python object
      
# Function to save tasks to the file  
def save_tasks(tasks): 
    """Saves the updated list of tasks to the JSON file.  
    Converts the Python object into a properly formatted JSON file.""" 
    with open(TODO_FILE, "w") as file: # Open the file in write mode  
        json.dump(tasks, file, indent=4) # Convert Python object to JSON and save with indentation for readability
        
@click.group() # Create cli group which let us define multiple commands
def cli():  #main cli group, returns nothing
    """Simple Todo List Manager"""
    pass

@click.command() # Create command to add task in the list
@click.argument("task") # Create argument to put task in the list through command
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task":task, "done":False}) #task is incompleted (by default)
    save_tasks(tasks)
    click.echo(f'Task added successfully: {task}') #print on the cli
  
@click.command() # Create command for list preview
def lst(): 
    tasks = load_tasks()
    if not tasks:
        click.echo("No task found!")
        return
    for index, task in enumerate(tasks, 1): # Loop through the tasks while giving index to each task starting from 1
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} [{status}]")
    
@click.command() # Create command to mark the task as completed
@click.argument("task_number", type=int) # Create argument to define the task number which is to be marked as done
def complete(task_number):
    """Mark task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True 
        save_tasks(tasks)
        click.echo(f"task {task_number} marked as completed")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command() # Create command to remove the task from the list
@click.argument("task_number", type=int) # Create the argument to define the task number which is to be removed
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo(f"Invalid task number: {task_number}")

# Registration of commands under CLI group       
cli.add_command(add)
cli.add_command(lst)
cli.add_command(complete)
cli.add_command(remove)

# To run the cli after the execution of script or file
if __name__ == "__main__":
    cli()
    
    
