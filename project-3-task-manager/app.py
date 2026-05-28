from flask import Flask, render_template, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn Docker"},
    {"id": 2, "task": "Learn Jenkins"}
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/api/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)