from flask import Flask, render_template, request, redirect, url_for
from models import Student, GraduateStudent
from storage import load_data, save_data

app = Flask(__name__)
students_db = load_data() or []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students")
def list_students():
    return render_template("students.html", students=students_db)

@app.route("/add_student", methods = ["POST", "GET"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        id = int(request.form["id"])
        gpa = float(request.form["gpa"])
        is_grad = request.form.get("is_grad")
        thesis = request.form.get("thesis", "")

        if is_grad:
            student = GraduateStudent(name, id, gpa, thesis)
        else:
            student = Student(name, id, gpa)
        
        students_db.append(student)
        save_data(students_db)

        return redirect(url_for("list_students"))
    
    return render_template("add_student.html")

@app.route("/edit_student/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    student = next((s for s in students_db if s.id == student_id), None)
    if not student:
        return "Student not found", 404
    if request.method == "POST":
        student.name = request.form["name"]
        student.gpa = float(request.form["gpa"])
        if isinstance(student, GraduateStudent):
            student.thesis = request.form.get("thesis", "")
        
        save_data(students_db)
        return redirect(url_for("list_students"))
    
    return render_template("edit_student.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)