from flask import Blueprint

students_bp = Blueprint('students', __name__)

from app_module.students import views