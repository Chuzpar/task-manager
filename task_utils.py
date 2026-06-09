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

def mark_task_as_complete(tasks, task_number):
    index = int(task_number) - 1

    if index >= 0 and index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Task not found")

def view_pending_tasks(tasks):
    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("No pending tasks")
        return

    for i in range(len(pending_tasks)):
        task = pending_tasks[i]
        print(f"{i + 1}. {task['title']} - {task['description']} - Due: {task['due_date']}")

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