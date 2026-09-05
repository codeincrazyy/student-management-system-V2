class Student:
    def __init__(self,id,name,age,email):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        
        
    def __str__(self):
        return f"student(id: {self.id}, name: {self.name}, age: {self.age}, email: {self.email})"