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
`\` - `GET` Root endpoint, brings you to the welcome page of the website<br/>
`\register` - `GET` Register endpoint, brings you to the page to sign up for an account (submit button calls `POST` and sends you to `\login`)<br/>
`\login` - `GET` Login endpoint, the page where you can login if you've already created an account (submit button calls `POST` and sends you to `\home`)<br/>
`\home` - `GET` Home page endpoint, welcomes the user and prompts for pokemon. (submit button calls `POST` and sends to `\results`)<br/>
`\results` - `GET` Result page for the search, gives you the song recommendation for the pokemon<br/>

### Architecture
We used the MVC (Model-View-Controller) architecture for our project
![image](https://github.com/user-attachments/assets/b549b3ec-f886-4e76-a51c-6ea49e8200ce)


