#!/usr/bin/python3
"""Export data from an API to a CSV file"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)

    if res.status_code != 200:
        print("User not found")
        sys.exit(1)

        user_name = res.json().get('username')
        task_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + user
        res = requests.get(task_url)
        tasks = res.json()

        with open('{}.csv'.format(user), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in tasks:
                completed = task.get('completed')
                title_task = task.get('title')
                csvwriter.writerow([user, user_name, completed, title_task])

