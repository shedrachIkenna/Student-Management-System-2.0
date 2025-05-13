from flask import Flask, jsonify, request
from flask_cors import CORS
import json, os 
from models import Student, GraduateStudent

app = Flask(__name__)
CORS(app)

DATA_FILE = "students.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        raw = json.load(f)
        students = []
        for item in raw:
            if item.get('type') == "GraduateStudent":
                students.append(GraduateStudent(item["name"], item["student_id"], item["gpa"], item["thesis_title"]))
            else:
                students.append(Student(item["name"], item["student_id"], item["gpa"]))
        return students
    
def save_data(students):
    with open(DATA_FILE, "w") as f:
        json.dump([s.to_dict() for s in students], f)


students_db = load_data()

# Routes 

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify([s.to_dict() for s in students_db])


@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.json
    new_id = max([s.student_id for s in students_db], default=0) + 1

    if data['type'] == "GraduateStudent":
        new_student = GraduateStudent(data["name"], new_id, data['gpa'], data["thesis_title"])
    else:
        new_student = Student(data['name'], new_id, data['gpa'])
    
    students_db.append(new_student)
    save_data(students_db)
    return jsonify(new_student.to_dict()), 201


@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.json
    for i, s in enumerate(students_db):
        if s.student_id == student_id:
            if data['type'] == "GraduateStudent":
                students_db[i] = GraduateStudent(data['name'], student_id, data['gpa'], data['thesis_title'])
            else:
                students_db[i] = Student(data['name'], student_id, data['gpa'])
            save_data(students_db)
            return jsonify(students_db[i].to_dict())
    return jsonify({"error": "Student not found"}), 404

@app.route("/api/students/<int:student_id>", methods=["DELETE"])  # Added int: type converter
def delete_student(student_id):
    global students_db 
    students_db = [s for s in students_db if s.student_id != student_id]  # Fixed attribute name
    save_data(students_db)
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)

