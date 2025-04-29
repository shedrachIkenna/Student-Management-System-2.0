class Student:
    def __init__(self, name, id, gpa):
        self.name = name 
        self.id = id 
        self.gpa = gpa 
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.id}")
        print(f"GPA: {self.gpa}")
    
    def __str__(self):
        return f"Name: {self.name} || Student ID: {self.id} || GPA: {self.gpa}"

class GraduateStudent(Student):
    def __init__(self, name, id, gpa, thesis):
        super().__init__(name, id, gpa)
        self.thesis = thesis    
    
    def display_info(self):
        super().display_info()
        print(f"Thesis Title: {self.thesis}")