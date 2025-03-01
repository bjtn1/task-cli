# TODO
# 1) work on add-task functionality
# 2) work on listing tasks
# 3) work on updatign task
# 4) mark as in-progress etc

import argparse
import json
import os
from datetime import datetime


def get_tasks(json_path):
    # we do a try...except because if tasks.json is empty,
    # we must create an empty json object
    # otherwise we'll get a JSONDecodeError
    try:
        # turning json files into dicts works like this:
        with open(json_path, "r") as json_file:
            tasks_dict = json.load(json_file)
    except (json.JSONDecodeError, FileNotFoundError):
        # create an empty json file if tasks.json is initially empty
        tasks_dict = {}

        # we create the file if it doesn't already exist
        with open(json_path, "w") as json_file:
            json.dump(tasks_dict, json_file)

    return tasks_dict



def add(task_description):
    tasks_dict = get_tasks("./tasks.json")

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
    # TODO
    # 1) open json file and turn it into a dict
    try
    with open("./tasks.json", "r") as json_file:
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
