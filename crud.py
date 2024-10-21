from models import db, Teacher, Student
from flask import jsonify

def create_teacher(data):
    new_teacher = Teacher(**data)
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({"message": "Teacher created", "id": new_teacher.id}), 201

def read_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return jsonify(teacher.__dict__)

def update_teacher(teacher_id, data):
    teacher = Teacher.query.get_or_404(teacher_id)
    for key, value in data.items():
        setattr(teacher, key, value)
    db.session.commit()
    return jsonify({"message": "Teacher updated"}), 200

def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    db.session.delete(teacher)
    db.session.commit()
    return jsonify({"message": "Teacher deleted"}), 200

# Аналогичные функции для Student (create_student, read_student, update_student, delete_student)