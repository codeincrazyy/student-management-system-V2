from student_manager import StudentManager
from student import Student



def main_menu(manager):
        
    start = input("enter option\nadd\nupdate\ndelete\nsearch\nadd many\n: ")
        
    match start:
            case 'add':
                name = input("enter name: ")
                age = input("enter age: ")
                email = input("enter email: ")
                
                student = Student(None,name,age,email)
        
                manager.add_student(student)
                
            case 'search':
                print("all users")
                for student in manager.view_students():
                    print(student)
            
            case 'delete':                
                id = input("enter id of user you want to delete: " )
                
                manager.delete_student(id)
                
            
            case 'update':
                id = input("enter id of user you want to update: " )
                
                
                email = input("enter the new email: ")
                
                manager.update_student(id,email)
        