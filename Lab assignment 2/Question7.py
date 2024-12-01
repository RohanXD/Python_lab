def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    if student_name:
        print(f"Student Name: {student_name}")
    if student_class:
        print(f"Student Class: {student_class}")
student_data(101)
student_data(102, student_name="Alice")
student_data(103, student_name="Bob", student_class="5th Grade")
