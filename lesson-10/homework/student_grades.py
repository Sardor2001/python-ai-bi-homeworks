import csv


# Step 0: Create grades.csv (if it doesn't exist)
def create_grades_file(filename):
    data = [
        {"Name": "Alice", "Subject": "Math", "Grade": 85},
        {"Name": "Bob", "Subject": "Science", "Grade": 78},
        {"Name": "Carol", "Subject": "Math", "Grade": 92},
        {"Name": "Dave", "Subject": "History", "Grade": 74}
    ]
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Subject", "Grade"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Created {filename} with initial data.")


# Step 1: Read data from grades.csv and store it in a list of dictionaries
def read_grades(filename):
    grades = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(row)
    return grades


# Step 2: Calculate the average grade for each subject
def calculate_average_grades(grades):
    subject_grades = {}
    for entry in grades:
        subject = entry['Subject']
        grade = int(entry['Grade'])
        if subject in subject_grades:
            subject_grades[subject].append(grade)
        else:
            subject_grades[subject] = [grade]

    average_grades = {}
    for subject, grades in subject_grades.items():
        average_grades[subject] = sum(grades) / len(grades)
    return average_grades


# Step 3: Write the average grades to a new CSV file
def write_average_grades(filename, average_grades):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, average in average_grades.items():
            writer.writerow([subject, average])


# Main program
if __name__ == "__main__":
    # Step 0: Create grades.csv (if it doesn't exist)
    create_grades_file('grades.csv')

    # Step 1: Read grades from grades.csv
    grades = read_grades('grades.csv')

    # Step 2: Calculate average grades
    average_grades = calculate_average_grades(grades)

    # Step 3: Write average grades to average_grades.csv
    write_average_grades('average_grades.csv', average_grades)

    print("Average grades have been calculated and written to average_grades.csv.")
