from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, make_response
from models.user import User
from models import db
import requests
from flask import session

users_bp = Blueprint('users_bp', __name__)

# Default page of the application: gives you login or register options
@users_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Registration page
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
        username = request.form['username']
        password = request.form['password']

        # Authenticate the user
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Verify the password
            # Store user ID in session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return render_template('home.html', user=user)

        flash('Invalid credentials. Please try again.', 'error')
        return redirect(url_for('users_bp.login'))

    return render_template('login.html')

# Home page
@users_bp.route('/home', methods=['GET'])
def home():
    # Retrieve the current user from the session
    user_id = session.get('user_id')  # Assuming 'user_id' is set during login
    if user_id:
        user = User.query.get(user_id)  # Fetch the user from the database
    else:
        user = None  # No user logged in

    return render_template('home.html', user=user)

# Logout route
@users_bp.route('/logout', methods=['POST'])
def logout():
    response = redirect(url_for('users_bp.index'))
    flash('You have been logged out.', 'success')
    return response

# Results route for Pokémon API
@users_bp.route('/results', methods=['POST', 'GET'])
def results():
    pokemon_info = None  # Default to no Pokémon data
    
    if request.method == 'POST':
        # Handle Pokémon API request
        pokemon_name = request.form.get('pokemon', '').strip().lower()
        if not pokemon_name:
            flash('Please enter a Pokémon name.', 'error')
        else:
            api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = requests.get(api_url)

            if response.status_code == 200:
                # If the API returns successfully, process the data
                pokemon_data = response.json()
                pokemon_info = {
                    'name': pokemon_data['name'].capitalize(),
                    'types': [t['type']['name'] for t in pokemon_data['types']],
                    'sprite': pokemon_data['sprites']['front_default']
                }
                return render_template('results.html', pokemon=pokemon_info)
            else:
                flash('Pokémon not found. Please check the name and try again.', 'error')

    return render_template('results.html')
