import { useEffect, useState } from 'react'

function App() {
  const [students, setStudents] = useState([])

  useEffect(() => {
    fetch('http:localhost:5000/api/students')
      .then(res => res.json())
      .then(data => setStudents(data))
      .catch(err => console.log("Failed to fetch students", err))
  }, [])
  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Management System</h1>
      <ul>
        {students.map((student) => {
          <li key={student.student_id}>
            <strong>{student.name}</strong> ({student.type}) - GPA: {student.gpa}
            {student.type == "GraduateStudent" && (
              <div>Thesis: {student.thesis_title}</div>
            )}
          </li>
        })}
      </ul>
    </div>
  )
}

export default App