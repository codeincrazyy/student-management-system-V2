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
        
        

    def create_from_db(self,table_row):
            
            new_instance = Student(table_row[0],table_row[1],table_row[2],table_row[3])
            
            
            return new_instance

#used to display data from a table
    def view_students(self):
        query = "SELECT * FROM users"

        try:
            with self.connection:
                table_row = self.connection.execute(query).fetchall()
                        
            return [self.create_from_db(row) for row in table_row]
                    
        except Exception as e:
                    print(e)
                    return[]
                

    def delete_student(self, student_id):
        select_query = "SELECT name FROM users WHERE id =?"
        delete_query = "DELETE FROM users WHERE id =? "
        
        
        try:
            with self.connection:
                
                cursor = self.connection.execute(select_query,(student_id,))
                
                student = cursor.fetchone()
                
                
                if student:
                    student_name = student[0]
                    
                    self.connection.execute(delete_query,(student_id,))
                    print(f"student {student_name} has been removed")
                else:
                    print(f"no student with id:{student_id} has been found")
                    
        except Exception as e:
            print(e)

    def update_student(self, student_id: int, name: str = None, age: int = None, email: str = None):
        
        fields = []
        params = []
        
        if email is not None:

            check_query = "SELECT * FROM users WHERE email = ? AND id != ?"
            
            cursor = self.connection.execute(check_query, (email, student_id))
            
            existing_student = cursor.fetchone()

            if existing_student:

                print(f"A student with email '{email}' already exists.")
                return
        
        if name is not None:
            fields.append("name = ?")
            params.append(name)
            
        if age is not None:
            fields.append("age = ?")
            params.append(age)
        
        if email is not None:
            fields.append("email = ?")
            params.append(email)
            
        if not fields:
            print("no updates been made.")
            return
        
        set_clause = ", ".join(fields)
        query = f"UPDATE users SET {set_clause} WHERE id = ?"
        params.append(student_id)
        
        try:
            with self.connection:
                cursor = self.connection.execute(query,tuple(params))
                
            if cursor.rowcount > 0:
                print("student info has been updated")
                
            else:
                print(f"no student found with ID:{student_id}")
            
        except sqlite3.IntegrityError:
                    print(f"a student with email '{email}' already exists.")
                    return False
            
    def find_student(self, student_id):
        query = "SELECT * FROM users WHERE id = ?"
        
        
        try:
            with self.connection:
                cursor = self.connection.execute(query, (student_id,))
                
                table_row = cursor.fetchone()
                
                if table_row:
                    return self.create_from_db(table_row)
        except Exception as e:
            print(e)
            
        
        
