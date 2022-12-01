#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    # get the given employees info
    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            argv[1]
        )
    ).json()

    # get the employees todo list
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
            argv[1]
        )
    ).json()

    # make it an actual list object
    todo_list = [
        {
            "USER_ID": argv[1],
            "USERNAME": employee["username"],
            "TASK_COMPLETED_STATUS": task["completed"],
            "TASK_TITLE": task["title"]
        } for task in todos
    ]

    # format and print response
    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        csv.DictWriter(
            f, quoting=csv.QUOTE_ALL, quotechar='"', fieldnames=[
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ]
        ).writerows(todo_list)
