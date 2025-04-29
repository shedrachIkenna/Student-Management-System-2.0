from flask import Flask, render_template, request, redirect, url_for
from models import Student, GraduateStudent
from storage import load_data, save_data

app = Flask(__name__)
students_db = load_data()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students")
def list_students():
    return render_template("students.html", students=students_db)

@app.route("/add_student")
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        id = int(request.form["id"])
        gpa = float(request.form["gpa"])
        is_grad = request.form.get["is_grad"]
        thesis = request.form.get["thesis", ""]

        if is_grad:
            student = GraduateStudent(name, id, gpa, thesis)
        else:
            student = Student(name, id, gpa)
        
        students_db.append(student)
        save_data(students_db)

        return redirect(url_for("list_students"))
    
    return render_template("add_student.html")


if __name__ == "__main__":
    app.run(debug=True)