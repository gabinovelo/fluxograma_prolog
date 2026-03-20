from models.user import User
from models.list import Register
from services.prolog_interface import verify_enrollment

user = User()
register = Register()

register.addCourse("vcalc", "Cálulo Vetorial", 1)
register.addCourse("calc1", "Cálculo I", 1)
register.addCourse("calc2", "Cálculo II", 2, ["calc1", "vcalc"])
register.addCourse("calc3", "Cálculo III", 3, ["calc2", "vcalc"])
register.addCourse("introprog", "Introdução à Programação", 1)
register.addCourse("poo", "Programação Orientada a Objetos", 2, ["introprog"])

for course in register.courses:
    print(f"ID: {course.id}")
    print(f"Nome: {course.name}")
    print(f"Semestre: {course.semester}")
    print(f"Pré-Requisitos: {course.requirements}\n")

print(user.history)
print(verify_enrollment(user.history, "calc3"))

print(verify_enrollment(user.history, "calc3"))