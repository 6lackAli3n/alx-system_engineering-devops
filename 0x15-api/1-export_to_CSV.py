#!/usr/bin/python3
"""Export data from an API to a CSV file"""
import csv
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

        # Write to CSV
        csv_filename = f'{user_id}.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                csvwriter.writerow([user_id, user_name, task.get('completed'), task.get('title')])
