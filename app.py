from flask import Flask, render_template, request, url_for, redirect
from database import get_database

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def root():
    db = get_database()
    cursor = db.execute("SELECT * FROM todolist")
    task_list = cursor.fetchall()
    return render_template("index.html", task_list=task_list)

@app.route("/inserttask", methods=["POST", "GET"])
def insert_task():
    if request.method == "POST":
        try:
            response = request.form["task"]
            db = get_database()
            cursor = db.cursor()
            cursor.execute("INSERT INTO todolist ( task) values(?)",[response])
            db.commit()
            db.close()
            return redirect(url_for("root"))
        except:
            db.rollback()
    return render_template("index.html")

@app.route("/deletetask/<int:id>", methods=["POST", "GET"])
def delete_task(id):
    if request.method == "GET":
        try:
            db = get_database()
            cursor = db.cursor()
            cursor.execute("DELETE FROM todolist WHERE id = ?",[id])
            db.commit()
            db.close()
            return redirect(url_for("root"))
        except:
            db.rollback()
    return render_template("index.html")

if __name__ == "__main___":
    app.run(debug=True, host="0.0.0.0", port=8080)