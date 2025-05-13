class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self.type = "Student"  # Add type for frontend differentiation
        
    def to_dict(self):  # Make sure this method exists and returns a dict
        return {
            "name": self.name,
            "student_id": self.student_id,
            "gpa": self.gpa,
            "type": self.type
        }

class GraduateStudent(Student):
    def __init__(self, name, student_id, gpa, thesis_title):
        super().__init__(name, student_id, gpa)
        self.thesis_title = thesis_title
        self.type = "GraduateStudent"
        
    def to_dict(self):
        data = super().to_dict()
        data["thesis_title"] = self.thesis_title
        return data