from run import app

app.app_context().push()

def test_students_after_login_success():
    with app.test_client() as client:
        client.post('/login',json={"email":"student123@school.in", "password":"Student123"})
        response = client.get('/students/students')
        client.get('/logout')
        assert response.status_code == 200

def test_students_after_login_failure():
    with app.test_client() as client:
        client.post('/login',json={"email":"teacher123@school.in", "password":"Teacher123"})
        response = client.get('/students/students')
        client.get('/logout')
        assert response.status_code == 403
        
def test_students_without_login():
    with app.test_client() as client:
        response = client.get('/students/students')
        assert response.status_code == 401
        
def test_post_enroll_students():
    with app.test_client() as client:
        client.post('login', json={"email":"student123@school.in", "password":"Student123"})
        response = client.post('/students/students/enroll', json={"teacher_id":"1"})
        client.get('/logout')
        json_response = response.get_json()
        assert response.status_code == 201

def test_post_again_enroll_students_same_teacher():
    with app.test_client() as client:
        client.post('login', json = {"email":"student123@school.in", "password":"Student123"})
        response = client.post('/students/students/enroll', json={"teacher_id":"1"})
        client.get('/logout')
        json_response = response.get_json()
        assert response.status_code == 400        
        
def test_post_enroll_students_unauthorized():
    with app.test_client() as client:
        client.post('/login', json={"email":"teacher123@school.in", "password":"Teacher123"})
        response = client.post('/students/students/enroll', json = {"teacher_id":"1"})
        client.get('/logout')
        json_response = response.get_json()
        assert response.status_code == 403

def test_post_enroll_students_404_teacher_():
    with app.test_client() as client:
        client.post('/login', json={"email":"student123@school.in", "password":"Student123"})
        response = client.post('/students/students/enroll', json = {"teacher_id":"8"}) #teacher_id that does not exist in teacher table
        client.get('/logout')
        json_response = response.get_json()
        assert response.status_code == 404       