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
    <h1>Student Management Student</h1>
  )
}

export default App