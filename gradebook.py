student = {}
student1 = {}

def add_student():
    name = input("Enter the student's name: ")
    if name not in student:
        student[name] = {}
        print(f"Student {name} added.")
    else:
        print("Student already exists.")

def add_subject():
    name = input("Enter the student's name: ")
    if name in student:
        n = int(input("Enter the number of subjects: "))
        for _ in range(n):
            subject = input("Enter subject: ")
            grade = float(input("Enter your grade: "))
            student[name][subject] = grade
        print(f"Subjects added for {name}.")
    else:
        print("Student not found.")

def calculate_avg():
    name = input("Enter the student's name: ")
    if name in student:
        grades = list(student[name].values())  # Convert dict_values to a list
        if grades:
            avg = sum(grades) / len(grades)
            student1[name] = avg
            print(f"Average grade for {name} is {avg}.")
        else:
            print("No grades available for this student.")
    else:
        print("Student not found.")

def display():
    no = int(input("Enter the number of students to display: "))
    for _ in range(no):
        name = input("Enter the student's name: ")
        if name in student1:
            print(f"Name: {name}, Average: {student1[name]}")
        else:
            print(f"No average found for {name}")

# Example sequence of function calls
add_student()        # Add a student
add_subject()        # Add subjects and grades for the student
calculate_avg()      # Calculate average grade for the student
display()            # Display the average grades for the student
