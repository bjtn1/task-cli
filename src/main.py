# TODO
# 1) work on add-task functionality
# 2) work on listing tasks
# 3) work on updatign task
# 4) mark as in-progress etc

import argparse
import json
import os
from datetime import datetime
"""
should I check if the file exists in every single function?
Perhaps we should check if it exists before calling any function
that would increase speed methinks


2) I dont think creating a global variable for the dictionary is a good idea.
I am going to add a dictionary as a paremeter to every function

better yet, i should be able to open the file inside each function and
scratch that, we should think about how we're going to represent each task
a task will be made up of:
- an id
- a name
- a status

its going to look like this



what a task will look like
{
    "id": {
        "description": "",
        "status": "",
        "createdAt": "",
        "updatedAt": "",
    },
}
"""


def add(task_description):
    # we do a try...except because if tasks.json is empty,
    # we must create an empty json object
    # otherwise we'll get a JSONDecodeError
    try:
        # turning json files into dicts works like this:
        with open("./tasks.json", "r") as json_file:
            tasks_dict = json.load(json_file)
    except (json.JSONDecodeError, FileNotFoundError):
        # create an empty json file if tasks.json is initially empty
        tasks_dict = {}

        # we create the file if it doesn't already exist
        with open("./tasks.json", "w") as json_file:
            tasks_dict = json.load(json_file)

    # count the total tasks in the json file
    total_tasks = len(tasks_dict)

    # create the unique id
    id = total_tasks + 1

    # format date in 2025-01-31 13:59:59 format
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # create the task that will be added to the json
    # the `updatedAt` field will be the same as the createdAt field whenever we add
    new_task = {
        "description": f"{task_description}",
        "status": "active",
        "createdAt": f"{date}",
        "updatedAt": f"{date}"
    }

    # add new task to the dict
    tasks_dict[id] = new_task
    
    # add the new task back to the file
    with open("./tasks.json", "w") as json_file:
        # convert the file back to a json file
        json.dump(tasks_dict, json_file, indent=4)

    print(f"Successfully added \"{task_description}\" (ID: {id})")


def update(task_id):
    print(f"updating {task_id}")
    pass


def delete(task):
    print(f"deleting {task}")
    pass

def list_tasks(status):
    pass


def main():
    parser = argparse.ArgumentParser(
        prog="task-cli",
        description="A simple CLI for keeping track of your tasks"
    )

    group = parser.add_mutually_exclusive_group(
        required=True,
    )

    group.add_argument(
        "-a",
        "--add",
    )

    group.add_argument(
        "-u",
        "--update",
        nargs=2,
    )

    group.add_argument(
        "-d",
        "--delete",
    )

    group.add_argument(
        "-l",
        "--list",
    )

    args = parser.parse_args()

    add_task = args.add
    update_task = args.update
    task_id = args.delete
    list_tasks = args.list

    # TODO
    # check that tasks.json exists before calling any function
    # if it doesn't exist, create the file
    if not os.path.exists("./tasks.json"):
        tasks_file = open("./tasks.json", "w")
        tasks_file.close()

    if add_task:
        add(add_task)
    elif update_task:
        update_task(update_task)
    elif task_id:
        delete(task_id)
    elif list_tasks:
        list_tasks()



if __name__ == "__main__":
    main()
