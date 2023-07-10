from flask import Flask, jsonify
import os

from flask_login import LoginManager
from app_module.models import db, User
from app_module.auth import auth_bp
from app_module.teachers import teachers_bp
from app_module.students import students_bp
from flask_migrate import Migrate


app = Flask(__name__)
app.config.update(
    SECRET_KEY="topsecret",
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:Akash%40123@localhost/catalog_db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

login_manager = LoginManager(app)
# login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return jsonify({"message": "Unauthorized"}), 401

db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
Migrate(app,db)

app.register_blueprint(auth_bp)
app.register_blueprint(teachers_bp, url_prefix='/teachers')
app.register_blueprint(students_bp, url_prefix='/students')

