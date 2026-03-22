from flask import Flask, render_template, request, jsonify
from models.list import Register
from models.user import User
from services.prolog_interface import verify_enrollment

app = Flask(__name__)

register = Register()
user = User()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = []
    for c in register.courses:
        available = verify_enrollment(user.history, c.id)
        cursed = c.id in user.history
        courses.append({
            "id": c.id,
            "name": c.name,
            "semester": c.semester,
            "requirements": c.requirements or [],
            "cursed": cursed,
            "available": available and not cursed,
        })
    return jsonify(courses)

@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.json
    id_ = data.get("id", "").strip().lower()
    name = data.get("name", "").strip()
    semester = int(data.get("semester", 1))
    requirements = [r.strip().lower() for r in data.get("requirements", []) if r.strip()]

    if not id_ or not name:
        return jsonify({"error": "ID e nome são obrigatórios"}), 400

    success = register.addCourse(id_, name, semester, requirements if requirements else None)
    if not success:
        return jsonify({"error": "Disciplina já cadastrada"}), 409

    return jsonify({"ok": True})

@app.route("/api/courses/<id_>", methods=["DELETE"])
def remove_course(id_):
    success = register.removeCourse(id_)
    if not success:
        return jsonify({"error": "Disciplina não encontrada"}), 404
    user.removeCourse(id_)
    return jsonify({"ok": True})

@app.route("/api/history", methods=["GET"])
def get_history():
    return jsonify(user.history)

@app.route("/api/history", methods=["POST"])
def add_history():
    data = request.json
    id_ = data.get("id", "").strip().lower()
    success = user.addCourse(id_)
    if not success:
        return jsonify({"error": "Já está no histórico"}), 409
    return jsonify({"ok": True})

@app.route("/api/history/<id_>", methods=["DELETE"])
def remove_history(id_):
    success = user.removeCourse(id_)
    if not success:
        return jsonify({"error": "Não está no histórico"}), 404
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)
