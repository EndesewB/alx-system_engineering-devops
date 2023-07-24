#!/usr/bin/python3

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the progress of an employee's todo tasks.

    Args:
        employee_id (int): The ID of the employee to fetch and display
                           todo progress for.

    Returns:
        None: The function prints the progress and completed task
              titles for the employee.

    Raises:
        None: If an error occurs during API requests or if the employee
              data is not found.

    Example:
        >>> get_employee_todo_progress(1)
        Employee Leanne Graham is done with tasks(8/20):
            eos ea quo neque officiis magnam officia soluta
            autem quasi aut nobis magnam consequuntur
            et eveniet perspiciatis optio est qui ea dolore
            laboriosam dolor voluptates
            ... (remaining completed tasks)
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        if user_response.status_code != 200 or
        todos_response.status_code != 200:
            print("Error: Employee data not found.")
            return

        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in
                              todos_data if task.get("completed"))

        print(f"Employee {employee_name} is done with tasks
              ({completed_tasks}/{total_tasks}): ")

        for task in todos_data:
            if task.get("completed"):
                print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
