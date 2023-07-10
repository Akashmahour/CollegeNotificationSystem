from flask import Blueprint

teachers_bp = Blueprint('teachers', __name__)

from app_module.teachers import views