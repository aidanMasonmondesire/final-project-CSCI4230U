from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from models.user import User
from models import db
from flask_jwt_extended import create_access_token

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Gather data from the HTML form
        username = request.form['username']
        password = request.form['password']

        # Check if the user already exists
        if User.query.filter_by(username=username).first():
            flash('User already exists. Please choose a different username.', 'error')
            return redirect(url_for('users_bp.register'))

        # Create a new user
        new_user = User(username=username)
        new_user.set_password(password)  # Assume set_password hashes the password
        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully! Please log in.', 'success')
        return redirect(url_for('users_bp.login'))

    return render_template('register.html')

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Gather data from the HTML form
        username = request.form['username']
        password = request.form['password']

        # Authenticate the user
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Assume check_password verifies the password
            access_token = create_access_token(identity=user.id)
            flash('Login successful!', 'success')
            # Optionally, store the token in session or cookies
            return redirect(url_for('users_bp.home'))

        flash('Invalid credentials. Please try again.', 'error')
        return redirect(url_for('users_bp.login'))

    return render_template('login.html')

@users_bp.route('/home')
def home():
    return render_template('home.html')