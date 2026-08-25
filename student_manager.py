from student import Student
import random

id_numbers = ("1","2","3","4","5","6","7","8","9","0")

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        student_id = "s"+"".join(random.choices(id_numbers, k=3))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        email = input("Enter student email: ")

        new_student = Student(student_id, name, age, email)

        self.students.append(new_student)
        
    def view_students(self):
        
        if not self.students:
            print("no students found.")
        
        for student in self.students:
            print(student)
            
    def search_student(self):
        target_id = input("enter student id: ")
        
        found = False
        
        for student in self.students:
            if target_id == student.id:
                print(student)
                found = True
                break
            
        if not found:
            print(f"no student with id '{target_id}' found")
                
    def delete_student(self):
        target_id = input("enter the the id of the student you want to remove: ")
        
        found = False
        
        for student in self.students:
            if target_id == student.id:
                self.students.remove(student)
                print(f"student {student.name} has been removed succsfully")
                found = True
                break
        if not found:
            print(f"no student with id '{target_id}' found")
            
    def update_student(self):
        target_id = input("enter the students id you want to modify: ")
        
        found = False
        
        for student in self.students:
            if target_id == student.id:
                print(student)
                while True:
                    print("what do you want to edit?")
                    try:
                        edit_option = int(input("1.Name\n2.Age\n3.Email\n: "))
                        break
                    except ValueError:
                        print("plaese enter a vaild input")
                    
                match edit_option:
                    case 1:
                        
                        print("edit name selected")
                        new_name = str(input("enter new name: "))
                        student.update_name(new_name)
                        print("student name has been updated successfully")
                        found = True
                        break
                    case 2:
                        print("edit age selected")
                        while True:
                            try:
                                new_age = int(input("enter new age: "))
                                student.update_age(new_age)
                                print("student age has been updated successfully")
                                found = True
                                break
                            except ValueError:
                                print("please enter an integer value only!")
                    case 3:
                        print("edit email selected")
                        new_email = str(input("enter new email: "))
                        student.update_email(new_email)
                        print("student email has been updated successfully")
                        found = True
                        break
                        
                        
                    case _:
                        print("invaild input")
                        break
            
        if not found:
                print(f"no student with id '{target_id}' found")
