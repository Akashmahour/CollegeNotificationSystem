from run import app,db
from app_module.models import User,Teacher,Student
app.app_context().push()

app.app_context().push()

def test_get_teachers_after_login_success():
    with app.test_client() as client:
        client.post("/login", json={"email":"teacher123@school.in", "password":"Teacher123"})
        response = client.get('/teachers/teachers')
        client.get('/logout')
        assert response.status_code == 200
        
def test_get_teachers_after_login_failure():
    with app.test_client() as client:
        client.post("/login", json={"email":"student123@school.in", "password":"Student123"})
        response = client.get('/teachers/teachers')
        client.get('/logout')
        assert response.status_code == 403
        
def test_get_teachers_without_login():
    with app.test_client() as client:
        response = client.get('/students/students')
        assert response.status_code == 401
        
def test_get_teachers_studdents():
    with app.test_client() as client:
        client.post("/login", json={"email":"teacher123@school.in", "password":"Teacher123"})
        response = client.get('/teachers/teachers/students')
        client.get('/logout')
        assert response.status_code == 200
        

def test_email():
    with app.test_client() as client:
        client.post("/login", json={"email":"teacher123@school.in", "password":"Teacher123"})
        response = client.post('/teachers/teachers/sendmail', json={"email": "teacher1234@school.in",
                             "password": "Teacher1234","subject" : "This is subject","message" : "How are you"})
        client.get('/logout')
        assert response.status_code == 200


            
def test_cleanup():
    user = User.query.filter_by(email="student123@school.in").first()
    stud = Student.query.filter_by(user_id=user.id).first()
    db.session.delete(stud)
    db.session.delete(user)
    db.session.commit()
    user = User.query.filter_by(email="teacher123@school.in").first()
    stud = Teacher.query.filter_by(user_id=user.id).first()
    db.session.delete(stud)

    db.session.delete(user)
    db.session.commit()
    
