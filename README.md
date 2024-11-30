# Final Project for CSCI4230U - Pokémend
## By Aidan Mason-Mondesire (100821742) & Jade Nguyen (100820863)

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

##### Run with Docker
Prerequisites: Install Docker Desktop from  [https://www.docker.com/get-started]
1.  Clone the repository.
```
git clone https://github.com/aidanMasonmondesire/final-project-CSCI4230U
```
2. Navigate to the root of the directory.
3. Open terminal and run `docker build -t pokemend .` to create the image
4. Then run the container with `docker run -d -p 5555:5555 pokemend`
5. Type `docker ps` to get the `CONTAINER ID`
6. use the `CONTAINER ID` to run `docker logs CONTAINER ID`
7. from there it should tell you where the server is running, follow the link and it will bring you to the website!

### API Endpoints
`\` - `GET` Root endpoint, brings you to the welcome page of the website<br/>
`\register` - `GET` Register endpoint, brings you to the page to sign up for an account (submit button calls `POST` and sends you to `\login`)<br/>
`\login` - `GET` Login endpoint, the page where you can login if you've already created an account (submit button calls `POST` and sends you to `\home`)<br/>
`\home` - `GET` Home page endpoint, welcomes the user and prompts for pokemon. (submit button calls `POST` and sends to `\results`)<br/>
`\results` - `GET` Result page for the search, gives you the song recommendation for the pokemon<br/>

### Architecture
We used the MVC (Model-View-Controller) architecture for our project
![image](https://github.com/user-attachments/assets/621f13e2-c01d-41de-aafa-f35bb406f998)

### Performance Review
![image](https://github.com/user-attachments/assets/28dc5e41-b87a-4ed3-a587-d6dfe87a2126)
Performance is very good based on the website's standards. The only problems with it were accessibility in terms of some of the html code, certain tags and labels were'nt included that should have been. (The project has been deployed through [https://render.com/] at [https://final-project-csci4230u.onrender.com/] but goes down after a period of time so is not currently able to be accessed)


