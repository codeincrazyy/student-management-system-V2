from student_manager import StudentManager
from menu import main_menu


def main():
    manager = StudentManager()
    main_menu(manager)

if __name__ == "__main__":
    main()