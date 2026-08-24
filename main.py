from student import Student
from student_manager import StudentManager

Student1 = Student("s001", "abigail", 22, "abigail@email.com")

Student2 = Student("s002", "able", 20, "able@email.com")

manager = StudentManager()

manager.add_student(Student1)
manager.add_student(Student2)

manager.view_student()

manager.update_student()