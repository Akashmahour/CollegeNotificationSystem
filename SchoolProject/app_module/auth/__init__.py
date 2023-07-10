from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from app_module.auth import views