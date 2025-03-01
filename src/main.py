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


def print_tasks(tasks_dict):
    print(
    f"Description: {tasks_dict["description"]}\n"
    f"Status: {tasks_dict["status"]}\n"
    f"Created at: {tasks_dict["createdAt"]}\n"
    f"Updated at: {tasks_dict["updatedAt"]}\n"
    )


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


def list_tasks(status: str):
    # set the whole status to lower case just to be safe
    if status is not None:
        status = status.lower()

    # open json file and turn it into a dict
    tasks_dict = get_tasks("./tasks.json")

    # iterate over the values of dict to look at each task's description
    # and be able to access the `status` field
    for task_id, task_info in tasks_dict.items():
        if status is None or task_info["status"] == status:
            print(f"ID: {task_id}")
            print_tasks(task_info)


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
        help="Add a new task",
    )

    group.add_argument(
        "-u",
        "--update",
        nargs=2,
        metavar=("TASK_ID", "NEW_STATUS"),
        help="Update the status of a task",
    )

    group.add_argument(
        "-d",
        "--delete",
        metavar="TASK_ID",
        help="Delete a taks by ID",
    )

    group.add_argument(
        "-l",
        "--list",
        nargs="?",
        const=None,
        metavar="STATUS",
        help="List all tasks by STATUS (prints all tasks if no STATUS is given)",
    )

    args = parser.parse_args()

    if args.add:
        add(args.add)
    elif args.update:
        update(*args.update)
    elif args.delete:
        delete(args.delete)
    elif args.list or args.list is None:
        list_tasks(args.list)



if __name__ == "__main__":
    main()
