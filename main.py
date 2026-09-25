from student import Student
from student_manager import StudentManager
from utils import (
    get_integer_input,
    get_non_empty_input,
    get_valid_age,
    get_valid_marks
)


manager = StudentManager()


def add_student():
    print("\n--- Add Student ---")

    student_id = get_integer_input("Enter Student ID: ")

    if manager.search_student(student_id) is not None:
        print("Student ID already exists!")
        return

    name = get_non_empty_input("Enter Name: ")
    age = get_valid_age("Enter Age: ")
    course = get_non_empty_input("Enter Course: ")
    marks = get_valid_marks("Enter Marks: ")

    student = Student(
        student_id,
        name,
        age,
        course,
        marks
    )

    if manager.add_student(student):
        print("Student added successfully!")
    else:
        print("Student ID already exists!")


def search_student():
    print("\n--- Search Student ---")

    student_id = get_integer_input("Enter Student ID: ")

    student = manager.search_student(student_id)

    if student:
        student.display()
    else:
        print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    student_id = get_integer_input("Enter Student ID: ")

    student = manager.search_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nCurrent Student Details:")
    student.display()

    name = get_non_empty_input("Enter New Name: ")
    age = get_valid_age("Enter New Age: ")
    course = get_non_empty_input("Enter New Course: ")
    marks = get_valid_marks("Enter New Marks: ")

    manager.update_student(
        student_id,
        name,
        age,
        course,
        marks
    )

    print("Student updated successfully!")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = get_integer_input("Enter Student ID: ")

    student = manager.search_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent to be deleted:")
    student.display()

    confirmation = input(
        "Are you sure you want to delete this student? (y/n): "
    )

    if confirmation.lower() == "y":

        if manager.delete_student(student_id):
            print("Student deleted successfully!")
        else:
            print("Student could not be deleted.")

    else:
        print("Delete operation cancelled.")

def view_result():
    print("\n--- View Student Result ---")

    try:
        student_id = int(input("Enter Student ID: "))

        student = manager.search_student(student_id)

        if student is None:
            print("Student not found.")
            return

        print("\n--- Student Result ---")
        print(f"Student ID : {student.student_id}")
        print(f"Name       : {student.name}")
        print(f"Course     : {student.course}")
        print(f"Marks      : {student.marks}")
        print(f"Grade      : {student.get_grade()}")
        print(f"Result     : {student.get_result()}")
        print("------------------------")

    except ValueError:
        print("Student ID must be a number.")


def main():

    while True:

        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Student")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            view_result()

        elif choice == "7":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()