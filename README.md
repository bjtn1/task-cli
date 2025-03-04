# Task CLI

A command-line program to create and keep track of your tasks.

## Author

- **Name:** Brandon Jose Tenorio Noguera  
- **Email:** [task_cli@bjtn.me](mailto:task_cli@bjtn.me)  
- **Website:** [https://bjtn.me](https://bjtn.me)  
- **GitHub:** [https://github.com/bjtn1](https://github.com/bjtn1)  
- **Inspiration:** [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)  

## Description

Task CLI is a simple command-line tool that allows users to manage tasks efficiently. You can add, update, delete, list, and mark tasks as completed with a few simple commands.

## Features

- Add tasks with descriptions
- Update task descriptions
- Delete tasks by ID
- List all tasks or filter by status
- Mark tasks with different statuses
- JSON-based task storage

## Installation

Clone the repository:
```sh
$ git clone https://github.com/bjtn1/task-cli.git
$ cd task-cli
```

Install dependencies (if any):
```sh
$ pip install -r requirements.txt  # No dependencies as of now
```

## Usage

Run the script:
```sh
$ python task_cli.py [OPTIONS]
```

### Available Commands

| Command | Description |
|---------|-------------|
| `-a "task description"`, `--add "task description"` | Add a new task |
| `-u TASK_ID "new description"`, `--update TASK_ID "new description"` | Update task description |
| `-m TASK_ID "new status"`, `--mark TASK_ID "new status"` | Change the status of a task |
| `-d TASK_ID`, `--delete TASK_ID` | Delete a task by ID |
| `-l [STATUS]`, `--list [STATUS]` | List all tasks or tasks by status |

### Example Usage

Add a new task:
```sh
$ python task_cli.py --add "Buy groceries"
```

Update a task:
```sh
$ python task_cli.py --update 1 "Buy groceries and cook dinner"
```

Mark a task as completed:
```sh
$ python task_cli.py --mark 1 "done"
```

Delete a task:
```sh
$ python task_cli.py --delete 1
```

List all tasks:
```sh
$ python task_cli.py --list
```

List only "todo" tasks:
```sh
$ python task_cli.py --list todo
```

## Considerations

- **Do you want to make this an executable?** You can use `pyinstaller` to create a standalone executable:
  ```sh
  $ pyinstaller --onefile task_cli.py
  ```
  This will generate an executable in the `dist/` directory.

## License

This project is licensed under the MIT License.

## Contributions

Feel free to contribute by submitting issues and pull requests on GitHub!


