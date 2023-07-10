from run import app

app.app_context().push()

def test_home_route():
    response = app.test_client().get('/login')
    assert response.status_code == 401
    json_response = response.get_json()
    assert json_response == {"message": "Invalid Request"}
    
def test_login_content():
    with app.test_client() as client:
        response = client.post('/login',json={"email":"admin@school.in"})
        json_response = response.get_json()
        assert response.status_code == 401
        assert json_response == {"message": "Invalid Request"}

def test_login_route_success():
    with app.test_client() as c:
        response = c.post('/login', json={"email":"admin@school.in", "password": "Admin"})
        json_response = response.get_json()
        assert response.status_code == 200
        assert json_response == {"message": "Logged in successfully"}    

def test_login_route_failure():
    with app.test_client() as c:
        response = c.post('/login', json={"email":"admin@school.in", "password": "Admin1"})
        json_response = response.get_json()
        assert response.status_code == 401
        assert json_response == {"message": "Invalid credentials"}
        
def test_logout_route():
    with app.test_client() as c:
        response = c.get('/logout')
        json_response = response.get_json()
        assert response.status_code == 200
        
        #assert json_response == {"message": "Logged out successfully"}
        assert "Logged out successfully" in json_response['message']
                
def test_register_teacher_without_login():
    with app.test_client() as c:
        response = c.post('/register/teacher', json={"teacher_name": "teacher123", "email": "teacher123@school.in", "password": "Teacher123"})
        json_response = response.get_json()
        assert response.status_code == 401
        
       # assert json_response == {"message": "Please login as Admin"}
        
def test_register_student_without_login():
    with app.test_client() as c:
        response = c.post('/register/student', json={"student_name": "student123", "email": "student123@school.in", "password": "Student123"})
        json_response = response.get_json()
        assert response.status_code == 401
        # assert json_response == {"message": "Please login as manager"}

def test_register_student_success():
    with app.test_client() as c:
        response = c.post('/login', json={"email":"manager@school.in", "password": "Manager"})
        json_response = response.get_json()
        assert response.status_code == 200
        response = c.post('/register/student', json={"student_name": "student123", "email": "student123@school.in", "password": "Student123"})
        json_response = response.get_json()
        assert response.status_code == 201
        
        # assert json_response == {"message": "Student registered successfully"}
def test_register_student_without_manager():
    with app.test_client() as c:
        response = c.post('/login', json={"email":"teacher123@school.in", "password":"Teacher123"})
        json_response = response.get_json()
        response = c.post('/register/student', json={"email":"student1234@school.in","student_name":"student1234", "password":"Student1234"})
        json_response = response.get_json()
        c.get('/logout')
        assert response.status_code == 400

def test_register_teacher_success():
    with app.test_client() as c:
        response = c.post('/login', json={"email":"admin@school.in", "password": "Admin"})
        json_response = response.get_json()
        assert response.status_code == 200
        response = c.post('/register/teacher', json={"teacher_name": "teacher123", "email": "teacher123@school.in", "password": "Teacher123"})
        json_response = response.get_json()
        assert response.status_code == 201
        
        # assert json_response == {"message": "Teacher registered successfully"}
        
def test_resgister_teacher_without_admin():
    with app.test_client() as c:
        response = c.post('/login', json={"email":"managerschool.in", "password":"manager"})
        json_response = response.get_json()
        #assert response.status_code == 200
        response = c.post('/register/teacher', json={"teacher_name": "teacher123", "email": "teacher123@school.in", "password": "Teacher123" })
        json_response = response.get_json()
        c.get('/logout')
        assert response.status_code == 400