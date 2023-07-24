#!/usr/bin/python3
"""
Fetches todo data from the JSONPlaceholder API and exports it to JSON format.

Usage:
    python3 todo_all_employees.py [USER_ID]

If a user ID is provided as an argument, it fetches and exports tasks for that specific user.
Otherwise, it fetches and exports all tasks from all employees.
"""

import requests
import sys
import json

def fetch_todo_data(user_id=None):
    """
    Fetches todo data from the JSONPlaceholder API.

    Args:
        user_id (int, optional): If provided, fetches tasks for a specific user.

    Returns:
        list: A list of tasks fetched from the API.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id} if user_id else {}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        sys.exit(1)

def export_to_json(data):
    """
    Organizes the fetched todo data into a dictionary of tasks for each user.

    Args:
        data (list): A list of tasks fetched from the API.

    Returns:
        dict: A dictionary where each key is the user ID, and the value is a list of tasks.
    """
    user_tasks = {}
    for task in data:
        user_id = str(task['userId'])
        username = task['title']
        task_title = task['title']
        completed = task['completed']

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user_tasks[user_id].append({
            "username": username,
            "task": task_title,
            "completed": completed
        })

    return user_tasks

def main():
    """
    Main function to fetch todo data and export it to JSON.

    If a user ID is provided as a command-line argument, it fetches and exports tasks for that specific user.
    Otherwise, it fetches and exports all tasks from all employees.
    """
    if len(sys.argv) == 2:
        user_id = sys.argv[1]
        data = fetch_todo_data(user_id)
        user_tasks = export_to_json(data)

        filename = f"{user_id}.json"
        with open(filename, 'w') as file:
            json.dump(user_tasks, file, indent=2)
    else:
        data = fetch_todo_data()
        user_tasks = export_to_json(data)

        filename = "todo_all_employees.json"
        with open(filename, 'w') as file:
            json.dump(user_tasks, file, indent=2)

if __name__ == "__main__":
    main()
