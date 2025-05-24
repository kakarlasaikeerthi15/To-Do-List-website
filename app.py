from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder="static")

USERS_FILE = "users.json"
TASKS_FILE = "tasks.json"

def load_data(file):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump({}, f)
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    users = load_data(USERS_FILE)
    if data["username"] in users:
        return jsonify({"success": False, "message": "User already exists"}), 409
    users[data["username"]] = data["password"]
    save_data(USERS_FILE, users)
    return jsonify({"success": True})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    users = load_data(USERS_FILE)
    if users.get(data["username"]) == data["password"]:
        return jsonify({"success": True})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route("/tasks/<username>", methods=["GET", "POST"])
def tasks(username):
    tasks = load_data(TASKS_FILE)
    if request.method == "POST":
        task = request.json.get("task")
        if not task or "title" not in task:
            return jsonify({"error": "Invalid task format"}), 400
        if "done" not in task:
            task["done"] = False
        tasks.setdefault(username, []).append(task)
        save_data(TASKS_FILE, tasks)

    user_tasks = tasks.get(username, [])
    filter_status = request.args.get("filter")
    sort_by = request.args.get("sort")

    if filter_status == "completed":
        user_tasks = [t for t in user_tasks if t.get("done")]
    elif filter_status == "incomplete":
        user_tasks = [t for t in user_tasks if not t.get("done")]

    if sort_by == "due_date":
        user_tasks.sort(key=lambda x: x.get("due_date") or "")
    elif sort_by == "status":
        user_tasks.sort(key=lambda x: x.get("done"))

    return jsonify(user_tasks)

@app.route("/tasks/<username>/<int:index>", methods=["PUT", "DELETE"])
def update_task(username, index):
    tasks = load_data(TASKS_FILE)
    user_tasks = tasks.get(username, [])

    if index >= len(user_tasks) or index < 0:
        return jsonify({"error": "Invalid task index"}), 404

    if request.method == "PUT":
        updated_task = request.json.get("task")
        if not updated_task:
            return jsonify({"error": "No task provided"}), 400
        user_tasks[index].update(updated_task)
    elif request.method == "DELETE":
        user_tasks.pop(index)

    tasks[username] = user_tasks
    save_data(TASKS_FILE, tasks)
    return jsonify(user_tasks)

if __name__ == "__main__":
    app.run(debug=True)