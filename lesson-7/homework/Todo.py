import os
import json
import csv
from abc import ABC, abstractmethod


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }


class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks, file_name):
        pass

    @abstractmethod
    def load(self, file_name):
        pass


class CSVStorage(StorageStrategy):
    def save(self, tasks, file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, file_name):
        tasks = []
        if os.path.exists(file_name):
            with open(file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task(**row))
        return tasks


class JSONStorage(StorageStrategy):
    def save(self, tasks, file_name):
        with open(file_name, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file)

    def load(self, file_name):
        tasks = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                data = json.load(file)
                for item in data:
                    tasks.append(Task(**item))
        return tasks


class TaskManager:
    def __init__(self, storage_strategy):
        self.tasks = []
        self.storage_strategy = storage_strategy

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                print("Current Task Details:", task)
                task.title = input("Enter New Title (leave blank to keep current): ") or task.title
                task.description = input("Enter New Description (leave blank to keep current): ") or task.description
                task.due_date = input("Enter New Due Date (YYYY-MM-DD, leave blank to keep current): ") or task.due_date
                task.status = input(
                    "Enter New Status (Pending/In Progress/Completed, leave blank to keep current): ") or task.status
                print("Task updated successfully!")
                return
        print("Error: Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with the given status.")
        else:
            for task in filtered_tasks:
                print(task)

    def save_tasks(self):
        file_name = input("Enter file name to save tasks: ")
        self.storage_strategy.save(self.tasks, file_name)
        print("Tasks saved successfully!")

    def load_tasks(self):
        file_name = input("Enter file name to load tasks: ")
        self.tasks = self.storage_strategy.load(file_name)
        print("Tasks loaded successfully!")

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.filter_tasks()
            elif choice == '6':
                self.save_tasks()
            elif choice == '7':
                self.load_tasks()
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Choose storage format:")
    print("1. CSV")
    print("2. JSON")
    format_choice = input("Enter your choice: ")

    if format_choice == '1':
        manager = TaskManager(CSVStorage())
    elif format_choice == '2':
        manager = TaskManager(JSONStorage())
    else:
        print("Invalid choice. Defaulting to CSV.")
        manager = TaskManager(CSVStorage())

    manager.menu()
