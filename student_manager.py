from student import Student

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        
    def view_student(self):
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
                print("removed succsfully")
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
                print("what do you want to edit?")
                try:
                    edit_option = int(input("1.Name\n 2.Age\n 3.Email\n"))
                except ValueError:
                    print("plaese enter a vaild input")
                    break
                    
                match edit_option:
                    case 1:
                        
                        print("edit name selected")
                        new_name = str(input("enter new name: "))
                        student.update_name(new_name)
                    case 2:
                        print("edit age selected")
                        while True:
                            try:
                                new_age = int(input("enter new age: "))
                                student.update_age(new_age)
                                print("age has been updated successfully")
                                break
                            except ValueError:
                                print("please enter an integer value only!")
                    case 3:
                        print("edit email selected")
                        new_email = str(input("enter new email: "))
                        student.update_email(new_email)
                        
                        found = True
                    case _:
                        print("invaild input")
                break
            
        if not found:
            print(f"no student with id '{target_id}' found")
