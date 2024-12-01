class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks
student = Student("abc", 85)

print("Original Values:")
print(f"Student Name: {student.student_name}")
print(f"Marks: {student.marks}")

student.student_name = "xyz"
student.marks = 90

print("\nModified Values:")
print(f"Student Name: {student.student_name}")
print(f"Marks: {student.marks}")
