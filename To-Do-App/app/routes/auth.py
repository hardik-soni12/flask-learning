from flask import Blueprint, render_template, redirect, request, flash, url_for, session
from app.forms import RegistrationForm, LoginForm
from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
         # check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Try logging in instead.', 'danger')
            return redirect(url_for('auth_bp.register'))
        
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            username = form.username.data,
            email = form.email.data,
            password = hashed_password
            )
        db.session.add(new_user)
        db.session.commit()
        flash ('Account created!!', 'success')
        return redirect(url_for('auth_bp.login'))
    return render_template('register.html', form = form)
        
@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id #store user id in session
            flash (f'Welcome {user.username}!', 'success')
            return redirect(url_for('task_bp.view_task'))
        else: 
            flash ('Invalid Email or Password!', 'danger')
    return render_template('login.html', form = form)


@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove User ID from session
    flash ('you haved been logged out!', 'info')
    return redirect(url_for('auth_bp.login'))