from flask import Blueprint
from app import db
from app.models.users import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return 'Home - sqlalchemy Structure Working!!'

@main_bp.route('/add')
def add_user():
    user = User(name = 'hardik', email = 'hardik9156@gmail.com', password = '123123123')
    db.session.add(user)
    db.session.commit()
    return 'User added!'