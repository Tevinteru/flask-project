import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from models import db, Teacher, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///technikum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Set the secret key

db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Define forms
class TeacherForm(FlaskForm):
    last_name = StringField('Фамилия', validators=[DataRequired()])
    first_name = StringField('Имя', validators=[DataRequired()])
    patronymic = StringField('Отчество')
    birthday = DateField('День рождения', format='%Y-%m-%d')
    subject = StringField('Предмет')
    education = StringField('Образование')
    experience = IntegerField('Стаж')
    phone = StringField('Телефон')
    email = StringField('E-mail', validators=[Email()])
    submit = SubmitField('Сохранить')

class StudentForm(FlaskForm):
    last_name = StringField('Фамилия', validators=[DataRequired()])
    first_name = StringField('Имя', validators=[DataRequired()])
    group = StringField('Группа')
    height = FloatField('Рост')
    birthday = DateField('День рождения', format='%Y-%m-%d')
    average_score = FloatField('Средний балл')
    library_card = BooleanField('Читательский билет')
    submit = SubmitField('Сохранить')

# Routes for CRUD operations with teachers
@app.route('/teachers', methods=['GET'])
def teachers():
    teachers = Teacher.query.all()
    return render_template('teachers.html', teachers=teachers)

@app.route('/teacher/create', methods=['GET', 'POST'])
def create_teacher():
    form = TeacherForm()
    if form.validate_on_submit():
        teacher = Teacher(
            last_name=form.last_name.data,
            first_name=form.first_name.data,
            patronymic=form.patronymic.data,
            birthday=form.birthday.data,
            subject=form.subject.data,
            education=form.education.data,
            experience=form.experience.data,
            phone=form.phone.data,
            email=form.email.data
        )
        db.session.add(teacher)
        db.session.commit()
        flash('Преподаватель добавлен!', 'success')
        return redirect(url_for('teachers'))
    return render_template('teacher_form.html', form=form, title='Добавить преподавателя')

@app.route('/teacher/<int:id>', methods=['GET'])
def get_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    return render_template('teacher_detail.html', teacher=teacher)

@app.route('/teacher/edit/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    form = TeacherForm(obj=teacher)
    if form.validate_on_submit():
        form.populate_obj(teacher)
        db.session.commit()
        flash('Информация о преподавателе обновлена!', 'success')
        return redirect(url_for('teachers'))
    return render_template('teacher_form.html', form=form, title='Редактировать преподавателя')

@app.route('/teacher/delete/<int:id>', methods=['POST'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    flash('Преподаватель удален!', 'success')
    return redirect(url_for('teachers'))

# Routes for CRUD operations with students
@app.route('/students', methods=['GET'])
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/student/create', methods=['GET', 'POST'])
def create_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            last_name=form.last_name.data,
            first_name=form.first_name.data,
            group=form.group.data,
            height=form.height.data,
            birthday=form.birthday.data,
            average_score=form.average_score.data,
            library_card=form.library_card.data
        )
        db.session.add(student)
        db.session.commit()
        flash('Студент добавлен!', 'success')
        return redirect(url_for('students'))
    return render_template('student_form.html', form=form, title='Добавить студента')

@app.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return render_template('student_detail.html', student=student)

@app.route('/student/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        form.populate_obj(student)
        db.session.commit()
        flash('Информация о студенте обновлена!', 'success')
        return redirect(url_for('students'))
    return render_template('student_form.html', form=form, title='Редактировать студента')

@app.route('/student/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Студент удален!', 'success')
    return redirect(url_for('students'))

if __name__ == '__main__':
    app.run(debug=True)