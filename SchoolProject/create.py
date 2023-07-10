# code to add admin and manager


from run import app, db
from app_module.models import User

app.app_context().push()
admin = User("admin@school.in", "Admin", "admin")
manager = User("manager@school.in", "Manager", "manager")
db.session.add_all([admin, manager])
db.session.commit()



# from run import app,db
# from app_module.models import User,Teacher,Student
# app.app_context().push()
# user = User.query.filter_by(email="student123@school.in").first()
# stud = Student.query.filter_by(user_id=user.id).first()
# db.session.delete(stud)
# db.session.delete(user)
# db.session.commit()
# user = User.query.filter_by(email="teacher123@school.in").first()
# stud = Teacher.query.filter_by(user_id=user.id).first()
# db.session.delete(stud)

# db.session.delete(user)
# db.session.commit()