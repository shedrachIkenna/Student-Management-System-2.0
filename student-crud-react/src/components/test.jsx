import { useState } from 'react'

function StudentForm(){
    const [name, setName] = useState("")
    const [gpa, setGpa] = useState("")
    const [type, setType] = useState("")
    const [thesis, setThesis] = useState("")

    const handleSubmit = async (e) => {
        const payload = {
            name, 
            gpa: parseFloat(gpa),
            type,
        }
        if (type == "GraduateStudent"){
            payload.thesis_title = thesis 
        }

        const res = await fetch("http://localhost/api/students", {
            method: "POST",
            headers: {
                "Content-Type": 'application/json'
            }, 
            body: JSON.stringify(payload)
        })

        newStudent = res.json()
        onStudentAdded(newStudent)

        setName("")
        setGpa("")
        setType("")
        setThesis("")
    }

    return (
       <div>
        <form onSubmit={handleSubmit}>
            <div>
                <label>Name:</label>
                <input value={name} onChange={(e) => setName(e.target.value)} required />
            </div>
            <div>
                <label>GPA:</label>
                <input value={gpa} onChange={(e) => setGpa(e.target.value)} type='number' step="0.01" required />
            </div>
            <div>
                <label>Type</label>
                <select value={type} onChange={(e) => setType(e.target.value)}>
                    <option value="Student">Student</option>
                    <option value="GraduateStudent">Graduate Student</option>
                </select>
            </div>
            {type == "GraduateStudent" && (
                <div>
                    <label>Thesis Title</label>
                    <input value={name} onChange={(e) => setThesis(e.target.value)} required />
                </div>
            )}
            <button type='submit'>Add Student</button>
        </form>
       </div>
    )
}

export default StudentForm