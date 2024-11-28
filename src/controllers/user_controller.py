from flask import Blueprint, request, render_template, redirect, url_for, flash
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
            print("no")
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

    # Mapping of songs to album covers
    song_to_album = {
        "Through the Fire and Flames by DragonForce": "/static/images/fire_album.jpg",
        "If only by The Marias": "/static/images/water_album.jpg",
        "Master of Puppets by Metallica": "/static/images/electric_album.jpg",
        "My Kind of Woman by Mac DeMarco": "/static/images/grass_album.jpg",
        "Goosebumps by Travis Scott": "/static/images/ghost_album.jpg",
        "Trust by Brent Faiyaz": "/static/images/poison_album.jpg",
        "Cove by Basement": "/static/images/dark_album.jpg",
        "Kingston by Faye Webster": "/static/images/fairy_album.jpg",
        "Redbone by Childish Gambino": "/static/images/normal_album.jpg",
        "What I've Done by Linkin Park": "/static/images/rock_album.jpg",
        "Brain Stew by Greenday": "/static/images/ground_album.jpg",
        "Sweet Lady by Queen": "/static/images/steel_album.jpg",
        "King For A Day by Pierce The Veil and Kellin Quinn": "/static/images/dragon_album.jpg",
        "TikTok by Ke$ha": "/static/images/psychic_album.jpg",
        "Hayloft by Mother Mother": "/static/images/bug_album.jpg",
        "PRIDE. by Kendrick Lamar": "/static/images/ice_album.jpg",
        "Pink + White by Frank Ocean": "/static/images/flying_album.jpg",
        "Pink Triangle by Weezer": "/static/images/fighting_album.jpg",
    }

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

                # Determine the song based on Pokémon types
                if 'fire' in pokemon_info['types']:
                    song_suggestion = "Through the Fire and Flames by DragonForce"  # Fire-type Pokémon
                elif 'water' in pokemon_info['types']:
                    song_suggestion = "If only by The Marias"  # Water-type Pokémon
                elif 'electric' in pokemon_info['types']:
                    song_suggestion = "Master of Puppets by Metallica"  # Electric-type Pokémon
                elif 'grass' in pokemon_info['types']:
                    song_suggestion = "My Kind of Woman by Mac DeMarco"  # Grass-type Pokémon (example)
                elif 'ghost' in pokemon_info['types']:
                    song_suggestion = "Goosebumps by Travis Scott"  # Grass-type Pokémon (example)
                elif 'poison' in pokemon_info['types']:
                    song_suggestion = "Trust by Brent Faiyaz"  # Grass-type Pokémon (example)
                elif 'dark' in pokemon_info['types']:
                    song_suggestion = "Covet by Basement"  # Grass-type Pokémon (example)
                elif 'fairy' in pokemon_info['types']:
                    song_suggestion = "Kingston by Faye Webster"  # Grass-type Pokémon (example)
                elif 'normal' in pokemon_info['types']:
                    song_suggestion = "Redbone by Childish Gambino"  # Grass-type Pokémon (example)
                elif 'rock' in pokemon_info['types']:
                    song_suggestion = "What I've Done by Linkin Park"  # Grass-type Pokémon (example)
                elif 'ground' in pokemon_info['types']:
                    song_suggestion = "Brain Stew by Greenday"  # Grass-type Pokémon (example)
                elif 'steel' in pokemon_info['types']:
                    song_suggestion = "Sweet Lady by Queen"  # Grass-type Pokémon (example)
                elif 'dragon' in pokemon_info['types']:
                    song_suggestion = "King For A Day by Pierce The Veil and Kellin Quinn"  # Grass-type Pokémon (example)
                elif 'psychic' in pokemon_info['types']:
                    song_suggestion = "TikTok by Ke$ha"  # Grass-type Pokémon (example)
                elif 'bug' in pokemon_info['types']:
                    song_suggestion = "Hayloft by Mother Mother"  # Grass-type Pokémon (example)
                elif 'ice' in pokemon_info['types']:
                    song_suggestion = "PRIDE. by Kendrick Lamar"  # Grass-type Pokémon (example)
                elif 'flying' in pokemon_info['types']:
                    song_suggestion = "Pink + White by Frank Ocean"  # Grass-type Pokémon (example)
                elif 'fighting' in pokemon_info['types']:
                    song_suggestion = "Pink Triangle by Weezer"  # Grass-type Pokémon (example)

                # Get the corresponding album cover
                album_cover = song_to_album.get(song_suggestion, "/static/images/default_album.jpg")

                # Retrieve the current user from the session
                user_id = session.get('user_id')  # Assuming 'user_id' is set during login

                if user_id:
                    user = User.query.get(user_id)  # Fetch the user from the database
                    # Assuming 'user' is a User instance
                    user.set_favourite_name(pokemon_info['name'])
                    user.set_favourite_types(pokemon_info['types'])
                    user.set_favourite_sprite(pokemon_info['sprite'])

                    db.session.commit()  # Save to database

                return render_template(
                    'results.html',
                    pokemon=pokemon_info,
                    song_suggestion=song_suggestion,
                    album_cover=album_cover
                )
            else:
                flash('Pokémon not found. Please check the name and try again.', 'error')

    return render_template('results.html')


@users_bp.route('/erase_favourite', methods=['GET', 'POST'])
def erase_favourite():
    user_id = session.get('user_id')

    if user_id:
        user = User.query.get(user_id)  # Fetch the user from the database
        user.set_favourite_name(None)  # Erase favourite Pokémon
        user.set_favourite_types(None)  # Erase favourite Pokémon types
        user.set_favourite_sprite(None)  # Erase favourite Pokémon sprite
        print(user.get_favourite_name)

        db.session.commit()  # Save changes to the database
        flash('Your favourite Pokémon has been erased!', 'success')
        return redirect(url_for('users_bp.home'))  # Redirect to the home page

    flash('You must be logged in to erase your favourite Pokémon.', 'error')
    return redirect(url_for('users_bp.login'))  # Redirect to login if not logged in
