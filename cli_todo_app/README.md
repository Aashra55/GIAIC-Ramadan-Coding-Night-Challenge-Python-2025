# CLI-Based To-Do List Management Application  

### Built with Python, `uv`, and `click`  

## Installation & Setup  

### 1. Install `uv`  
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Initialize the Project  
```sh
uv init todo-cli
```

### 3. Install `click` and Set Up the Virtual Environment inside your Project 
```sh
uv add click
```

### 4. Activate the Virtual Environment  
**Windows:**  
```sh
.venv\Scripts\activate
```
**Mac/Linux:**  
```sh
source .venv/bin/activate
```

## Usage  

### 1. Add a Task  
```sh
uv run python todo.py add "task description"
```

### 2. Mark a Task as Completed  
```sh
uv run python todo.py complete task_number
```
Example:  
```sh
uv run python todo.py complete 1
```

### 3. Remove a Task  
```sh
uv run python todo.py remove task_number
```
Example:  
```sh
uv run python todo.py remove 2
```

### 4. View the To-Do List  
```sh
uv run python todo.py lst
```
