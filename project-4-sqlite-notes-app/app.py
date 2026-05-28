from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)


@app.route("/")
def home():
    notes = Note.query.all()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    note_text = request.form.get("note")

    if note_text:
        new_note = Note(task=note_text)
        db.session.add(new_note)
        db.session.commit()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete_note(id):
    if 0 <= id < len(note):
        note.pop(id)

    return redirect("/")
    
@app.route("/complete/<int:id>")
def complete_note(id):
    note = Note.query.get(id)
    if note:    
            note.done = True
            db.session.commit()    

    return redirect("/")

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_note(id):
    note = Note.query.get(id)
    if request.method == "POST":

        updated_task = request.form.get("note")
        note.task = updated_task
        db .session.commit()
        return redirect("/")

    return render_template("edit.html", note=notes[index], index=index)

with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)