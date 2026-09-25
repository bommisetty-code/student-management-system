import json

from student import Student


class StudentManager:

    def __init__(self):
        self.students = []
        self.file_name = "students.json"
        self.load_students()

    # Add Student
    def add_student(self, student):

        if self.search_student(student.student_id) is not None:
            return False

        self.students.append(student)
        self.save_students()

        return True

    # View All Students
    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        print("\n--- All Students ---")

        for student in self.students:
            student.display()

    # Search Student
    def search_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                return student

        return None

    # Update Student
    def update_student(
        self,
        student_id,
        name,
        age,
        course,
        marks
    ):

        student = self.search_student(student_id)

        if student is None:
            return False

        student.name = name
        student.age = age
        student.course = course
        student.marks = marks

        self.save_students()

        return True

    # Delete Student
    def delete_student(self, student_id):

        student = self.search_student(student_id)

        if student is None:
            return False

        self.students.remove(student)

        self.save_students()

        return True

    # Save Students to JSON
    def save_students(self):

        data = []

        for student in self.students:
            data.append(student.to_dict())

        try:

            with open(self.file_name, "w") as file:
                json.dump(data, file, indent=4)

        except OSError as error:

            print(f"Error saving students: {error}")

    # Load Students from JSON
    def load_students(self):

        try:

            with open(self.file_name, "r") as file:
                data = json.load(file)

            for item in data:

                student = Student(
                    item["student_id"],
                    item["name"],
                    item["age"],
                    item["course"],
                    item["marks"]
                )

                self.students.append(student)

        except FileNotFoundError:

            self.students = []

        except json.JSONDecodeError:

            print("Warning: students.json contains invalid data.")
            self.students = []

        except OSError as error:

            print(f"Error loading students: {error}")
            self.students = []