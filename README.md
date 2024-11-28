# Final Project for CSCI4230U - Pokémend
## By Aidan Mason-Mondesire & Jade Nguyen

### About the Project
This is the final project for CSCI4230U in which we made a web application that uses Pokéapi to retrieve the information about a pokémon of the users choice,
we then recommend a song that they might like based on the type that they chose.
### How to Run Locally
1. Clone the repository.
```
git clone https://github.com/aidanMasonmondesire/final-project-CSCI4230U
```
2. Create a virtual environment.
```
python -m venv .venv
```
3. Install Dependencies.
```
pip install -r requirements.txt
```
4. Navigate to app.py and run it.
5. Open 'http://127.0.0.1:5555' on your browser.
### API Endpoints
`\` - `GET` Root endpoint, brings you to the welcome page of the website
`\register` - `GET` Register endpoint, brings you to the page to sign up for an account (submit button calls `POST` and sends you to `\login`)
`\login` - `GET` Login endpoint, the page where you can login if you've already created an account (submit button calls `POST` and sends you to `\home`)
`\home` - `GET` Home page endpoint, welcomes the user and prompts for pokemon. (submit button calls `POST` and sends to `\results`)
`\results` - `GET` Result page for the search, gives you the song recommendation for the pokemon

### Architecture
We used the MVC (Model-View-Controller) architecture for our project

