class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def get_grade(self):

        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"
    def get_result(self):

        if self.marks >= 50:
            return "PASS"
        else:
            return "FAIL"


    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course} - {self.marks}"
    

    def display(self):
        print(f"ID     : {self.student_id}")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print(f"Marks  : {self.marks}")
        print(f"Grade  : {self.get_grade()}")
        print(f"Result : {self.get_result()}")
        print("-" * 30)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }


class GraduateStudent(Student):

    def __init__(self, student_id, name, age, course, marks, specialization):
        super().__init__(student_id, name, age, course, marks)
        self.specialization = specialization

    def display(self):
        print(f"ID            : {self.student_id}")
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Course        : {self.course}")
        print(f"Specialization : {self.specialization}")
        print(f"Marks         : {self.marks}")
        print(f"Grade         : {self.get_grade()}")
        print(f"Result        : {self.get_result()}")
        print("-" * 35)