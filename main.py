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

def update_student():
    id = int(input("Enter student ID to update student credentials: "))

    for student in students_db:
        if student.id == id:
            print("\nCurrent information")
            student.display_info()

            print("What would you like to update? ")
            print("1. Name")
            print("2. GPA")
            if isinstance(student, GraduateStudent):
                print("3. Thesis")

            choice = input("Enter choice (1/2/3): ")
            if choice == "1":
                new_name = input("Enter new name: ")
                student.name = new_name
            elif choice == "2":
                new_gpa = float(input("Enter new GPA: "))
                student.gpa = new_gpa
            elif choice == "3" and isinstance(student, GraduateStudent):
                new_thesis = input("Enter new thesis title: ")
                student.thesis = new_thesis
            else:
                print("Invalid choice!")
                return
            
            print("\nStudent info updated successfully!")
            student.display_info()
            return
    print("Student not found!")


create_student()

print("ALL STUDENTS IN THE SYSTEM")
for student in students_db:
    print(student)

read_student()
update_student()