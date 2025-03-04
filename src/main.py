import argparse
import json
from datetime import datetime


def get_tasks(json_path: str) -> dict[int, dict[str, str]]:
    # TEST
    """
    Returns a dictionary that represents a list of tasks.
    Creates `tasks.json` in the current directory if it doesn't already exist

    json_path -- a string representation of the path to a file named `tasks.json` where all tasks are stored
    """
    # we do a try...except because if tasks.json is empty,
    # we must create an empty json object
    # otherwise we'll get a JSONDecodeError
    try:
        # turning json files into dicts works like this:
        with open(json_path, "r") as json_file:
            # this gives you a dict of the tasks in the json file
            tasks_dict: dict[int, dict[str, str]] = json.load(json_file)
    except (json.JSONDecodeError, FileNotFoundError):
        # create an empty json file if tasks.json is initially empty, or tasks.json doesn't exist
        tasks_dict: dict[int, dict[str, str]] = {}

        # we create the file if it doesn't already exist
        with open(json_path, "w") as json_file:
            json.dump(tasks_dict, json_file)

    # https://docs.python.org/3/library/json.html#json.dump
    # json.dump converts everything into a string, but we want the ID to be an int
    # so we convert each id into an int
    # and return that instead
    return {int(k): v for k, v in tasks_dict.items()}


def print_task(task_dict: dict[str, str]) -> None:
    # TEST
    """
    Prints a dictionary that represents a sigular task in the following form:
    Description: DESCRIPTION
    Status: STATUS
    Created at: CREATED_AT
    Updated at: UPDATED_AT
    """

    print(
    f"Description: {task_dict["description"]}\n"
    f"Status: {task_dict["status"]}\n"
    f"Created at: {task_dict["createdAt"]}\n"
    f"Updated at: {task_dict["updatedAt"]}\n"
    )


def add(task_description: str) -> None:
    # TEST
    """
    Adds "task_description" to `tasks.json` with the default status of "todo"
    Creates `tasks.json` if the file doesn't exist.


    task_description -- A string representing the description of a task. i.e.: "Clean garage"
    """
    # get the current tasks as a dict
    tasks_dict: dict[int, dict[str, str]] = get_tasks("./tasks.json")

    # create the unique id
    # to avoid problems with delete and overwriting existing entries
    # we have to find the max id in the dict, and increment that
    # the code below turns all the keys into an integer and finds the max ID
    # max_id will be 0 if tasks_dict is empty
    max_id: int = max(map(int, tasks_dict.keys())) if tasks_dict else 0

    task_id: int = max_id + 1

    # format the date in 2025-01-31 13:59:59 format
    date: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # create the task that will be added to the json
    # the `updatedAt` field will be the same as the createdAt field whenever we add
    new_task: dict[str, str] = {
        "description": f"{task_description}",
        "status": "todo",
        "createdAt": f"{date}",
        "updatedAt": f"{date}"
    }

    # add new task to the dict
    tasks_dict[task_id] = new_task
    
    # add the new task back to the file
    with open("./tasks.json", "w") as json_file:
        # convert the file back to a json file
        json.dump(tasks_dict, json_file, indent=4)

    print(f"Successfully added \"{task_description}\" (ID: {task_id})")


def update(task_id: int, new_task_description: str) -> None:
    # TEST
    """
    Updates an existing task in the file `tasks.json` by changing its description

    task_id -- an int representing an existing task in `tasks.json`
    new_task_description -- a str representing the new task description
    """

    # TODO
    # what if the user inputs a task_id that doesn't exist?

    tasks_dict: dict[int, dict[str, str]] = get_tasks("./tasks.json")

    # make sure task_id exists in the json file
    if task_id not in tasks_dict:
        raise KeyError(f"ID: {task_id} not found")

    old_task: dict[str, str] = tasks_dict[task_id]
    old_task["description"] = f"{new_task_description}"

    date: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    old_task["updatedAt"] = f"{date}"

    # write the change back to the json file
    with open("./tasks.json", "w") as json_file:
        json.dump(tasks_dict, json_file, indent=4)


def delete(task_id: int) -> None:
    # TODO
    # docstring
    """
    """
    # TEST
    tasks_dict: dict[int, dict[str, str]] = get_tasks("./tasks.json")

    # make sure key exists bfore deleting it
    if task_id in tasks_dict:
        del tasks_dict[task_id]
        with open("./tasks.json", "w") as json_file:
            json.dump(tasks_dict, json_file, indent=4)


def list_tasks(status: str) -> None:
    # TEST
    # set the whole status to lower case just to be safe
    # since we save it as a lowercase word in the json file
    if status is not None:
        status = status.lower()

    # open json file and turn it into a dict
    tasks_dict: dict[int, dict[str, str]] = get_tasks("./tasks.json")

    # iterate over the values of dict to look at each task's description
    # and be able to access the `status` field
    for task_id, task_info in tasks_dict.items():
        if status is None or task_info["status"] == status:
            print(f"ID: {task_id}")
            print_task(task_info)


def mark(task_id: int, new_status: str) -> None:
    # TODO
    tasks_dict: dict[int, dict[str, str]] = get_tasks(".tasks.json")

    task_to_be_changed: dict[str, str] = tasks_dict[task_id]

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
        help="Add a new task",
    )

    group.add_argument(
        "-u",
        "--update",
        nargs=2,
        metavar=("TASK_ID", "NEW_DESCRIPTION"),
        help="Update the description of a task",
    )

    group.add_argument(
        "-m",
        "--mark",
        nargs=2,
        metavar=("TASK_ID", "NEW_STATUS"),
        help="Update the status of a task",
    )

    group.add_argument(
        "-d",
        "--delete",
        metavar="TASK_ID",
        type=int,
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
        task_id: str = args.update[0]
        new_task_description: str = args.update[1]

        # if the task_id is not a digit, we cannot convert it to an int, so we throw an exception
        if not task_id.isdigit():
            raise ValueError(f"Expected an integer, but got {type(task_id)} instead.")
        else:
            # task_id will be a str since we got it from the command line
            # so we turn it into an int here iff it's safe
            update(int(task_id), new_task_description)
    elif args.mark:
        task_id: str = args.mark[0]
        new_status: str = args.mark[1]

        # if the task_id is not a digit, we cannot convert it to an int, so we throw an exception
        if not task_id.isdigit():
            raise ValueError(f"Expected an integer, but got {type(task_id)} instead.")
        else:
            # task_id will be a str since we got it from the command line
            # so we turn it into an int here iff it's safe
            mark(int(task_id), new_status)
    elif args.delete:
        delete(args.delete)
    elif args.list or args.list is None:
        list_tasks(args.list)



if __name__ == "__main__":
    main()
