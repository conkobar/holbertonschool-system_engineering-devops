#!/usr/bin/python3
"""exports data in json format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    # get the given employees info
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/"
    ).json()

    # get the employees todo list
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/"
    ).json()

    # make it an actual list object
    user_info = {
        user['id']: user['username'] for user in users
    }
    tasks = {
        [
                task['userId']: {
                    'username': user_info[task['userId']],
                    'task': task['title'],
                    'completed': task['completed']
                }
        ]
    }

    # format and print response
    with open("todo_all_employees.json", "w") as f:
        json.dump(tasks, f)
