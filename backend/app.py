from flask import Flask, request, jsonify
from flask_cors import CORS

import time
import psycopg2

app = Flask(__name__)
CORS(app)


conn = None

while conn is None:
    try:
        conn = psycopg2.connect(
            host="db",
            database="notesdb",
            user="postgres",
            password="postgres",
            port="5432"
        )
        print("Connected to DB")
    except:
        print("Waiting for database...")
        time.sleep(5)
# Home route
@app.route("/")
def home():
    return jsonify({"message": "Flask Backend Running"})


# Get all notes
@app.route("/notes", methods=["GET"])
def get_notes():
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes")
    rows = cur.fetchall()

    notes = []
    for row in rows:
        notes.append({
            "id": row[0],
            "title": row[1],
            "content": row[2]
        })

    cur.close()
    return jsonify(notes)


# Add note
@app.route("/notes", methods=["POST"])
def add_note():
    data = request.json
    title = data["title"]
    content = data["content"]

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notes (title, content) VALUES (%s,%s)",
        (title, content)
    )
    conn.commit()
    cur.close()

    return jsonify({"message": "Note added"})


# Update note
@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):
    data = request.json
    title = data["title"]
    content = data["content"]

    cur = conn.cursor()
    cur.execute(
        "UPDATE notes SET title=%s, content=%s WHERE id=%s",
        (title, content, id)
    )
    conn.commit()
    cur.close()

    return jsonify({"message": "Note updated"})


# Delete note
@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):

    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id=%s", (id,))
    conn.commit()
    cur.close()

    return jsonify({"message": "Note deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)