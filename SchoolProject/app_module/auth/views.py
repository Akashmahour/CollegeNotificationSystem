from flask import request, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from app_module.models import User, Teacher, db, Student
from app_module.auth import auth_bp
# import jwt


@auth_bp.route('/register/teacher', methods=['POST'])
@login_required
def register_teacher():
    if not current_user.role == "admin":
        return jsonify({"message": "Admin Authentication Required",}),401
    data = request.get_json()
    email = data['email']
    password = data['password']
    teacher_name = data['teacher_name']

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'Email already exists'}), 400

    user = User(email=email,password=password, role='teacher')
    db.session.add(user)
    db.session.commit()

    teacher = Teacher(name=teacher_name, user=user)
    db.session.add(teacher)
    db.session.commit()

    return jsonify({'message': 'Teacher registered successfully'}), 201

@auth_bp.route('/register/student', methods=['POST'])
@login_required
def register_student():

    if not current_user.role == "manager":
        return jsonify({"message": "Manager Authentication Required",}),401
    
    data = request.get_json()
    email = data['email']
    password = data['password']
    student_name = data['student_name']

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'Email already exists'}), 400

    user = User(email=email,password=password, role='student')
    db.session.add(user)
    db.session.commit()

    student = Student(name=student_name, user=user)
    db.session.add(student)
    db.session.commit()

    return jsonify({'message': 'Student registered successfully'}), 201

@auth_bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        data = request.get_json()
        
        if len(data.items()) != 2:
            return jsonify({"message": "Invalid Request",}), 401
        email = data['email']
        password = data['password']
        
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({'message': 'Invalid credentials'}), 401

        login_user(user)
        # print(current_user.role)
        # token = jwt.encode({'user_id': user.id}, "topsecret")
        return jsonify({'message': 'Logged in successfully'}), 200

    elif request.method == "GET":
        return jsonify({"message": "Invalid Request",}),401


@auth_bp.route('/logout')
@login_required
def logout():
    try:
        user = current_user.email
        logout_user()
        return jsonify({'message': f'{user} Logged out successfully'}), 200
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500

