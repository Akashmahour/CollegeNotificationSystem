from app_module import app
from app_module.models import db

if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)