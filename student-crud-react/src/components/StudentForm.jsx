import { useState } from 'react'

function StudentForm({ onStudentAdded }){
    const [name, setName] = useState("")
    const [gpa, setGpa] = useState("")
    const [type, setType] = useState("")
    const [thesis, setThesis] = useState("")

    const handleSubmit = async (e) => {
        console.log("test")
        e.preventDefault()
        const payload = {
            name, 
            gpa: parseFloat(gpa), 
            type,
        }

        if (type === "GraduateStudent"){
            payload.thesis_title = thesis
        }

        const res = await fetch("http://localhost:5000/api/students", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        })

        const newStudent = await res.json();
        onStudentAdded(newStudent)

        // Reset form
        setName("");
        setGpa("");
        setType("Student");
        setThesis("");
    }

    return(
        <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
            <h2>Add Student</h2>
            <div>
                <label>Name: </label>
                <input value={name} onChange={(e) => setName(e.target.value)} required/>
            </div>
            <div>
                <label>GPA:</label>
                <input value={gpa} onChange={(e) => setGpa(e.target.value)} required/>
            </div>
            <div>
                <label>Type:</label>
                <select value={type} onChange={(e) => setType(e.target.value)}>
                    <option value="Student">Student</option>
                    <option value="GraduateStudent">Graduate Student</option>
                </select>
            </div>
            {type === "GraduateStudent" && (
                <div>
                    <label>Thesis Title:</label>
                    <input value={thesis} onChange={(e) => setThesis(e.target.value)} required/>
                </div>
            )}
            <button type='submit'>Add Student</button>
        </form>
    )
}

export default StudentForm 