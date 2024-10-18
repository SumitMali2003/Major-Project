import json

# Task class to represent each task
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    # Mark the task as completed
    def mark_completed(self):
        self.completed = True

    # Display the task details in a readable format
    def __repr__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"Title: {self.title} | Category: {self.category} | Status: {status}\nDescription: {self.description}\n"

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Function to display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    tasks.append(Task(title, description, category))
    print(f"Task '{title}' added successfully!")

# Function to mark a task as completed
def mark_task_completed(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1].mark_completed()
        print(f"Task '{tasks[task_number - 1].title}' marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task.title}' deleted successfully!")
    else:
        print("Invalid task number.")

# Main menu function to interact with the user
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
