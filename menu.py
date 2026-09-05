from student_manager import StudentManager
from student import Student
import re


def main_menu(manager):
    
    def input_checker(prompt: str, min_val: int = None, max_val:int = None) -> int:
        while True:
            try:
                
                user_input = int(input(prompt))
                
            
                if min_val is not None and user_input < min_val:
                    print(f"value must be at least {min_val}")
                    continue
                
                if max_val is not None and user_input > max_val:
                    print(f"value can not exceed {max_val}")
                    continue
                
                return user_input
            
            except ValueError:
                print("please enter an integer value")
    
    def validate_name(prompt: str, min_length: int):
        
        while True:
            user_input = input(prompt).strip()
            
            if not user_input:
                print("input can not be empty or just spaces.please try again")
                continue
            
            if len(user_input) < min_length:
                print(f"must be at least {min_length} characters long.")
                continue
            
            return user_input
    
    def validate_email(prompt: str):
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$"
            
            while True:
                user_input = input(prompt)
                
                if not user_input:
                    print("email can not be empty.please try again")
                    continue
                    
                if not re.match(email_pattern, user_input):
                    print("invalied email format.(example: student@example.com)")
                    continue
                
                return user_input
    
    while True:    
        print("====student managemnt system====")
        start = input("\n1.add student\n2.update student info\n3.remove student\n4.view all student\n5.find a student\n6.exit\n:")
            
        match start:
                case '1':
                    name = validate_name("enter name: ", min_length=2)
                    age = input_checker("enter age: ", min_val=4, max_val=24)
                    email = validate_email("enter email: ")
                    
                    student = Student(None,name,age,email)
            
                    manager.add_student(student)
                    
                case '4':
                    print("all students")
                    for student in manager.view_students():
                        print(student)
                
                case '3': 
                            id = input_checker("enter id of the student you want to remove: ",min_val=1 )
                            manager.delete_student(id)
                            
                    
                
                case '2':
                    id = input_checker("enter id of user you want to update: ",min_val=1 )
                    
                    name = validate_name("enter the new name: ",min_length=2)
                    age = input_checker("enter the new age: ",min_val=4,max_val=24)
                    email = validate_email("enter the new email: ")
                    
                    manager.update_student(id,name,age,email)
                    
                case '5':
                    id = input_checker("enter id of the student: ",min_val=1)
                    
                    student = manager.find_student(id)
                    if student:
                        print(student)
                    else:
                        print(f"no student with id '{id}'found.")
                case '6':
                    print("exiting program\nGoodbye!")
                    
                    break
            