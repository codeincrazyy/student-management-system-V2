from student_manager import StudentManager
from student import Student

manager = StudentManager()

def main_menu(manager):
    
    while True:
        print("STUDENT MANAGEMENT SYSTEM")
        try:
            main_option = int(input("1.Add Student\n2.View Student\n3.Search Student\n4.Update Student\n5.Delete Student\n6.Exit\n: "))
        except ValueError:
                print("please enter an integer value")
                continue


        match main_option:
            case 1:
                print("Add Student selceted\n")
                manager.add_student()
            case 2:
                print("view student selected\n")
                manager.view_students()
            case 3:
                print("search student selected\n")
                manager.search_student()
            case 4:
                print("update student selected\n")
                manager.update_student()
            case 5:
                print("delete student selected\n")
                manager.delete_student()
            case 6:
                print("exiting program\ngoodbye!")
                break
            case _:
                print("invaild choice!please choose between 1-6")
            
        