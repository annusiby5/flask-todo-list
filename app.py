from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("task")
    if task_text:
        tasks.append({"id": len(tasks), "text": task_text, "completed": False})
    return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return redirect(url_for("index"))

@app.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
