import os


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_record(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"

    @staticmethod
    def from_record(record):
        employee_id, name, position, salary = record.strip().split(',')
        return Employee(employee_id, name, position, float(salary))


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        self.employees = self.load_employees()

    def load_employees(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r") as file:
            return [Employee.from_record(line) for line in file.readlines()]

    def save_employees(self):
        with open(self.FILE_NAME, "w") as file:
            for employee in self.employees:
                file.write(employee.to_record() + "\n")

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = float(input("Enter Salary: "))
        self.employees.append(Employee(employee_id, name, position, salary))
        self.save_employees()
        print("Employee added successfully!")

    def view_employees(self):
        if not self.employees:
            print("No employee records available.")
        else:
            print("Employee Records:")
            for employee in self.employees:
                print(employee)

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")
        for employee in self.employees:
            if employee.employee_id == employee_id:
                print("Employee Found:", employee)
                return
        print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        for employee in self.employees:
            if employee.employee_id == employee_id:
                print("Current Details:", employee)
                employee.name = input("Enter New Name (leave blank to keep current): ") or employee.name
                employee.position = input("Enter New Position (leave blank to keep current): ") or employee.position
                salary_input = input("Enter New Salary (leave blank to keep current): ")
                employee.salary = float(salary_input) if salary_input else employee.salary
                self.save_employees()
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        initial_count = len(self.employees)
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        if len(self.employees) < initial_count:
            self.save_employees()
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
