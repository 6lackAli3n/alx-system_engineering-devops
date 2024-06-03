#!/usr/bin/python3
"""Export data from an API to a JSON file"""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/"
    todos_url = requests.get(url + "todos", params={"userId": user_id}).json()
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todos]}, jsonfile)
