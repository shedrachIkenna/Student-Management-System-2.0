from student_api.models import Student, GraduateStudent
from storage import save_data, load_data

students_db = load_data()

def create_student():
    try:
        name = input("Enter student name: ")
        id = int(input("Enter student ID: "))

        # Prevent duplicate ID
        if any(s.id == id for s in students_db):
            print("A student with this ID already exists")
            return
        
        gpa = float(input("Enter student GPA: "))
        is_grad = input("Are you a graduate (y/n): ")

        if is_grad == "y":
            thesis = input("Enter thesis title: ")
            new_student = GraduateStudent(name, id, gpa, thesis)
        else:
            new_student = Student(name, id, gpa)
        
        students_db.append(new_student)
        save_data()
        print(f"{name} added successfully")
    except ValueError:
        print(f"Invalid input. ID must be an integer and GPA must be a number!")


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
            
            save_data()
            print("\nStudent info updated successfully!")
            student.display_info()
            return
    print("Student not found!")

def delete_student():
    id = int(input("Enter student ID you want to delete"))

    for student in students_db:
        if student.id == id:
            confirm = input(f"Are you sure you want to delete {student.name}? (y/n)").lower()
            if confirm == "y":
                students_db.remove(student)
                save_data()
                print(f"Student {student.name} deleted successfully")
            else:
                print("Deletion cancelled")
            return
    
    print("Student not found")


def list_all_students():
    if not students_db:
        print("No students found!")
    else:
        print("\nAll Students: ")
        for students in students_db:
            print(students)

def main():
    load_data()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. List all Students")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            create_student()
        elif choice == "2":
            read_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            list_all_students()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("invalid option, Try again!")

main()