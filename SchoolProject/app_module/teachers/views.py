from flask import jsonify, request
from flask_login import login_required, current_user
from app_module.models import Teacher, User
from app_module.teachers import teachers_bp

@teachers_bp.route('/teachers', methods=['GET'])
@login_required
def get_teachers():
    if current_user.role == 'student':
        return jsonify({'message': 'Unauthorized access'}), 403

    teachers = Teacher.query.all()
    teacher_list = [{'id': teacher.id, 'name': teacher.name} for teacher in teachers]
    return jsonify(teacher_list), 200

# to get the students which are registered under the teacher
@teachers_bp.route('/teachers/students', methods=['GET'])
@login_required
def get_teacher_students():
    if current_user.role != 'teacher':
        return jsonify({'message': 'Unauthorized access'}), 403

    teacher_id = current_user.id
    teacher = Teacher.query.filter_by(user_id=teacher_id).first()
    if not teacher:
        return jsonify({'message': 'Teacher not found'}), 404

    students = teacher.students
    student_list = [{'id': student.id, 'name': student.name} for student in students]
    return jsonify(student_list), 200

@teachers_bp.route('/teachers/sendmail', methods=['POST'])
@login_required
def sendmail():
    if current_user.role != 'teacher':
        return jsonify({'message': f'{current_user.email} Unauthorized access'}), 403
    
    data = request.get_json()
    teacher_email = data.get("email")
    password = data.get("password")
    subject = data.get("subject")
    message = data.get("message")
    
    teacher_id = current_user.id
    teacher = Teacher.query.filter_by(user_id=teacher_id).first()
    students = teacher.students
    student_emails =[]
    for student in students:
        name = student.name
        email = User.query.filter_by(id = student.user_id).first().email
        student_emails.append({'name':name, 'email':email, "mail_message":f"Hello {name}," + message})
        
    # we can remove the password from here , we'll need the password if we have to login in the third party app to send the email    
    output = {"user_emial":teacher_email, "password":password, "mail_subject":subject, "recipients":student_emails}
    return jsonify(output), 200
        
        
    