from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

def add_task(tasks, title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(tasks, title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            print("Task marked as complete!")
            return

    print("Task not found")

def view_pending_tasks(tasks):
    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("No pending tasks")
        return

    for task in pending_tasks:
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print()

def calculate_progress(tasks):
    if len(tasks) == 0:
        print("No tasks currently")
        return 0

    completed_count = 0

    for task in tasks:
        if task["completed"]:
            completed_count += 1

    progress = (completed_count / len(tasks)) * 100

    print(f"Progress: {progress:.2f}%")
    return progress