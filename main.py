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
        super.__init__(name, id, gpa)
        self.thesis = thesis    

students_db = []

def create_student():
    name = input("Enter student name: ")
    id = int(input("Enter student ID: "))
    gpa = float(input("Enter student GPA: "))
    is_grad = input("Are you a graduate (y/n): ")

    if is_grad == "y":
        thesis = input("Enter thesis title: ")
        new_student = GraduateStudent(name, id, gpa, thesis)
    else:
        new_student = Student(name, id, gpa)
    
    students_db.append(new_student)
    print("{name} added successfully")


def read_student():
    id = int(input("Enter student ID to view student info: "))

    found = False 
    for student in students_db:
        if student.id == id:
            print("\nStudent Found: ")
            student.display_info()
            found = True 
            break
    
    if not found:
        print("Student not found!\n")

create_student()

print("ALL STUDENTS IN THE SYSTEM")
for student in students_db:
    print(student)