from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    patronymic = db.Column(db.String(80))
    birthday = db.Column(db.Date)
    subject = db.Column(db.String(120))
    education = db.Column(db.String(120))
    experience = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    group = db.Column(db.String(20))
    height = db.Column(db.Float)
    birthday = db.Column(db.Date)
    average_score = db.Column(db.Float)
    library_card = db.Column(db.Boolean)