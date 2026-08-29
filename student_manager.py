import sqlite3
from student import Student

class StudentManager:
    
    #crates your database
    def __init__(self, db_name: str = "database.db"):
        try:
            self.db_name = db_name
            self.connection = sqlite3.connect(self.db_name)
            self.create_table()
            
        except Exception as e:
            print(f"error: {e}")
            raise
            
    #crates the table 
    def create_table(self):
        query = """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    email TEXT UNIQUE
                )
        """
        try:
            with self.connection:
                self.connection.execute(query)
            print("table was created")
        except Exception as e:
            print(e)
        

    #used to insert data into the database
    def add_student(self, student: Student) -> bool:
        query = "INSERT INTO users(name,age,email) VALUES(?,?,?)"
        
        try:
            with self.connection:
                cursor = self.connection.execute(query,(student.name,student.age,student.email))
                
                print(f"user: {student.name} was added to the database!")
                
                student.id = cursor.lastrowid
                
                return True
            
        except sqlite3.IntegrityError:
            print(f"a student with email {student.email} already exists.")
            return False
        
        

#used to display data from a table
    def view_students(self):
        query = "SELECT * FROM users"

        try:
                with self.connection:
                    rows = self.connection.execute(query).fetchall()
                return rows
        except Exception as e:
            print(e)
            return[]

    def delete_student(self, user_id):
        query = "DELETE FROM users WHERE id =?"
        
        try:
            with self.connection:
                self.connection.execute(query,(user_id,))
                print(f"user has been deleted")
        except Exception as e:
            print(e)

    def update_student(self, user_id, email):
        query = "UPDATE users SET email = ? WHERE id = ?"
        
        try:
            with self.connection:
                self.connection.execute(query,(email,user_id))
                print("user info been updated")
        except Exception as e:
            print(e)
