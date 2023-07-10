from flask import jsonify, current_app, request
from flask_login import current_user, login_required
from app_module.models import Student, Teacher,db
from app_module.students import students_bp

@students_bp.route('/students', methods=['GET'])

@login_required
def get_students():
    if current_user.role == 'teacher':
        return jsonify({'message': 'Unauthorized access'}), 403

    students = Student.query.all()
    student_list = [{'id': student.id, 'name': student.name} for student in students]
    return jsonify(student_list), 200

@students_bp.route('/students/enroll', methods=['POST'])
@login_required
def enroll_student():
    if current_user.role != 'student':
        return jsonify({'message': 'Unauthorized access'}), 403

    student_id = current_user.id
    teacher_id = request.json.get('teacher_id')
    teacher = Teacher.query.filter_by(id=teacher_id).first()
    if not teacher:
        return jsonify({'message': 'Teacher not found'}), 404

    student = Student.query.filter_by(user_id=student_id).first()
    # if not student:
    #     return jsonify({'message': 'Student not found'}), 404

    if student in teacher.students:
        return jsonify({'message': 'Student already enrolled under this teacher'}), 400

    teacher.students.append(student)
    db.session.commit()

    return jsonify({'message': 'Student enrolled successfully'}), 201