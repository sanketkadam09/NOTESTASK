import React, { useState, useEffect } from "react";
import "./App.css";

function App() {

  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const API = "http://localhost:5000";

  const fetchNotes = async () => {
    const res = await fetch(`${API}/notes`);
    const data = await res.json();
    setNotes(data);
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  const addNote = async () => {
    await fetch(`${API}/notes`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ title, content })
    });

    setTitle("");
    setContent("");
    fetchNotes();
  };

  const deleteNote = async (id) => {
    await fetch(`${API}/notes/${id}`, {
      method: "DELETE"
    });

    fetchNotes();
  };

  return (
    <div className="container">

      <h1>DevOps Notes App</h1>

      <div className="form">
        <input
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <textarea
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />

        <button onClick={addNote}>Add Note</button>
      </div>

      <div className="notes">

        {notes.map((note) => (
          <div className="card" key={note.id}>
            <h3>{note.title}</h3>
            <p >{note.content}</p>

            <button onClick={() => deleteNote(note.id)}>
              Delete
            </button>

          </div>
        ))}

      </div>

    </div>
  );
}

export default App;