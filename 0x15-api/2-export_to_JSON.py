#!/usr/bin/python3
"""Export data from an API to a JSON file"""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

        user_data = user_response.json()
        user_name = user_data.get('username')

        # Fetch todos
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Prepare data for JSON export
        tasks = []
        for task in todos:
            task_dict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user_name
                    }
            tasks.append(task_dict)

            # Create JSON object
            json_data = {user_id: tasks}

            # Write to JSON file
            json_filename = f'{user_id}.json'
            with open(json_filename, 'w') as jsonfile:
                json.dump(json_data, jsonfile)
