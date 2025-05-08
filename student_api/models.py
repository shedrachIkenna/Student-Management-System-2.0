class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name 
        self.student_id = student_id
        self.gpa = gpa 
    
    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.tudent_id,
            "gpa": self.gpa,
            "type": "Student"
        }

class GraduateStudent(Student):
    def __init__(self, name, id, gpa, thesis_title):
        super().__init__(name, id, gpa)
        self.thesis_title = thesis_title   
    
    def to_dict(self):
        base = super().to_dict()
        base["thesis_title"] = self.thesis_title
        base["type"] = GraduateStudent
        return base 