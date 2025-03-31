import json
import csv

def load_tasks(filename):
    """Load tasks from a JSON file."""
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON.")
        return []

def display_tasks(tasks):
    """Display all tasks with their details."""
    if not tasks:
        print("No tasks to display.")
        return

    print("\nTasks:")
    print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Task Name", "Completed", "Priority"))
    print("-" * 45)
    for task in tasks:
        print("{:<5} {:<20} {:<10} {:<10}".format(
            task['id'], task['task'], str(task['completed']), task['priority']
        ))

def modify_task(tasks):
    """Modify a task based on user input."""
    task_id = int(input("Enter the ID of the task to modify: "))
    for task in tasks:
        if task['id'] == task_id:
            print(f"Current Task: {task['task']}")
            print(f"Current Completed Status: {task['completed']}")
            print(f"Current Priority: {task['priority']}")

            # Update task fields
            task['task'] = input("Enter new task name (or press Enter to keep current): ") or task['task']
            completed_input = input("Is the task completed? (yes/no, or press Enter to keep current): ").lower()
            if completed_input == "yes":
                task['completed'] = True
            elif completed_input == "no":
                task['completed'] = False
            priority_input = input("Enter new priority (or press Enter to keep current): ")
            if priority_input:
                task['priority'] = int(priority_input)

            print("Task updated successfully!")
            return
    print(f"Error: Task with ID {task_id} not found.")

def save_tasks(filename, tasks):
    """Save tasks to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to '{filename}'.")

def calculate_task_stats(tasks):
    """Calculate and display task completion statistics."""
    if not tasks:
        print("No tasks available to calculate statistics.")
        return

    # Calculate statistics
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks

    # Display statistics
    print("\nTask Completion Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def json_to_csv(json_filename, csv_filename):
    """Convert JSON data from tasks.json to a CSV file."""
    try:
        # Load JSON data
        with open(json_filename, 'r') as json_file:
            tasks = json.load(json_file)

        # Write to CSV
        with open(csv_filename, 'w', newline='') as csv_file:
            # Define CSV column headers
            fieldnames = ['ID', 'Task', 'Completed', 'Priority']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write rows
            for task in tasks:
                writer.writerow({
                    'ID': task['id'],
                    'Task': task['task'],
                    'Completed': task['completed'],
                    'Priority': task['priority']
                })

        print(f"Data successfully converted to '{csv_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{json_filename}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{json_filename}' contains invalid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = 'tasks.json'
    tasks = load_tasks(filename)

    while True:
        print("\nMenu:")
        print("1. Display Tasks")
        print("2. Modify a Task")
        print("3. Calculate Task Statistics")
        print("4. Convert JSON to CSV")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            modify_task(tasks)
        elif choice == '3':
            calculate_task_stats(tasks)
        elif choice == '4':
            json_to_csv(filename, 'tasks.csv')
        elif choice == '5':
            save_tasks(filename, tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()