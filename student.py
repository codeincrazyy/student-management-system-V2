class Student:
    def __init__(self, id, name, age, email ):
        
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        
    def update_age(self, age):
        self.age = age
        
    def update_email(self,email):
        self.email = email
        
    def update_name(self,name):
        self.name = name
        
    def __str__(self):
        return(f"id: {self.id}, name: {self.name}, age: {self.age}, email: {self.email}")
        
    
