#!/usr/bin/python3
"""
Python script that, using this REST API,
 for a given employee ID,
 returns information about his/her TODO list progress.
"""

import requests
import sys

def fetch_todo_list(employee_id):
    # URLs for the employee and TODO list endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        # Fetch employee information
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Fetch TODO list information
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    
    # Parse the JSON responses
    user = user_response.json()
    todos = todos_response.json()
    
    # Extract employee name
    employee_name = user.get('name')
    
    # Calculate task statistics
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)
    
    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the employee ID")
        sys.exit(1)
    
    fetch_todo_list(employee_id)
