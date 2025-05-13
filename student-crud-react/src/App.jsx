import { useEffect, useState } from 'react'
import StudentForm from './components/StudentForm'

function App() {
  const [students, setStudents] = useState([])

  useEffect(() => {
    fetch('http://localhost:5000/api/students')
      .then(res => res.json())
      .then(data => setStudents(data))
      .catch(err => console.log("Failed to fetch students", err))
  }, [])

  const handleAdd = (newStudent) => {
    setStudents([...students, newStudent])
  }

  const handleDelete = async (id) => {
    await fetch(`http://localhost:5000/api/students/${id}`, {
      method: "DELETE",
    });
    setStudents(students.filter((s) => s.student_id !== id));
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Management System</h1>
      <StudentForm onStudentAdded={handleAdd} />
      <ul>
        {students.map((student) => (
          <li key={student.student_id}>
            <strong>{student.name}</strong> ({student.type}) - GPA: {student.gpa}
            {student.type == "GraduateStudent" && (
              <div>Thesis: {student.thesis_title}</div>
            )}
            <button onClick={() => handleDelete(student.student_id)} style={{ marginLeft: "10px" }}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App