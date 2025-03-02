import os


def add_employee():
    try:
        emp_id = input("Enter Employee ID: ")
        if not emp_id.isdigit():
            raise ValueError("Employee ID must be a number.")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        if not salary.isdigit():
            raise ValueError("Salary must be a number.")

        with open("employees.txt", "a") as file:
            file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def view_employees():
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No employee records found.")
                return
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No employee records found.")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found:", line.strip())
                    return
        print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    found = False
    new_lines = []
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    found = True
                    name = input("Enter new name: ")
                    position = input("Enter new position: ")
                    salary = input("Enter new salary: ")
                    if not salary.isdigit():
                        raise ValueError("Salary must be a number.")
                    new_lines.append(f"{emp_id}, {name}, {position}, {salary}\n")
                else:
                    new_lines.append(line)
        if not found:
            print("Employee not found.")
            return
        with open("employees.txt", "w") as file:
            file.writelines(new_lines)
        print("Employee record updated successfully!")
    except FileNotFoundError:
        print("No employee records found.")
    except ValueError as e:
        print(f"Error: {e}")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False
    new_lines = []
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    found = True
                else:
                    new_lines.append(line)
        if not found:
            print("Employee not found.")
            return
        with open("employees.txt", "w") as file:
            file.writelines(new_lines)
        print("Employee record deleted successfully!")
    except FileNotFoundError:
        print("No employee records found.")


def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
