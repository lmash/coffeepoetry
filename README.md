# Coffee Poetry
The idea behind the website is for coffee to inspire poetry.
The website allows one to add and review a café, and then AI generates a poem 
based on the café and coffee descriptions provided.

## Poetry Generation Explained
- Poetry generation runs after each review is entered
- Only cafés with an average rating of 4 or higher and 3 or more review descriptions can generate poetry
- The AI uses a combination of the café and coffee descriptions (3 coffee descriptions are randomly selected) to generate a haiku

## Tech Stack
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)

### Setup Pre-Requisite
To enable poetry generation requires an API key from OpenAI. The website will work without the key
but will not be able to generate new poetry.

To get an OpenAI API Key
1. Visit platform.openai.com and sign in with an OpenAI account
2. Click your profile icon at the top-right corner of the page and select "View API Keys."
3. Click "Create New Secret Key" to generate a new API key.
4. Note the key created.

### Installation
1. Clone the repo and then change folder

```sh
git clone https://github.com/?????
cd lmash
```

2. Create a virtual environment 

```sh
python -m venv myenv
```

3. Install required packages

```shell
pip install -r requirements.txt
```

### One time poetry generation setup
1. Copy file: coffee/.env.example to coffee/.env
2. Open .env and paste the OpenAI key noted after 
`OPENAI_API_KEY=`
3. Save and close .env file

## Run
`python manage.py runserver`

### Distinctiveness and Complexity
The website is distinctive as it's main use is to review and advertise speciality cafès.
This is done using a traditional review system, along with a creative component - the Poetry generation 
part of the website which is there to encourage users to return and review frequently, and is only available for highly rated 
cafès.

The complexity comes from incorporating the review system and it's rules along with the AI generation of poems.
A café is reviewed based on 5 criteria, with the overall review updated and redisplayed after each review. 
The review is displayed using stars and the numeric value can be seen when hovering over the stars. Incorporating the AI
poem generation required some prompt engineering and combining details of the café and the review description.

The website has been deployed and is available at: www.????

### Page Descriptions
## Register
A page to create new accounts.Has validation to ensure the user being created is unique, 
all fields are populated and the passwords entered match.

## Login
User must enter username and password to login (once they've registered). Has validation to ensure
username and password entered match an existing account.

## CoffeePoetry
Displays all cafés ordered by review score, with the highest appearing first. Anyone (logged in/not) can see the same detail.
Shows the first image loaded against a café, the café name, location and a haiku and it's inspiration if one has been generated. Hover over inspiration to see.
Clicking on a cafés name displays the cafés page.

## \<User\> Cafés
Displays all cafés created by the user logged in, ordered by review score, with the highest appearing first. 
Clicking on a cafés name displays the cafés page.

## New Cafe
Allows a logged in user to create a café. Name, location, description and at least one image are mandatory.
The first image added will be displayed on all list pages for the café.

## Café
Displays a single café with a carousel of images, café name, location, description and rating.
Users logged in can review a café by clicking the Review button. The user who created the Café
can edit the description and add more images.

Clicking on the Review button displays a review window, the user can then rate the café using 5 criteria.
The user can also describe the coffee. After a review is saved the review (stars display) is updated, review criteria are reset 
and the poem is refreshed. Hovering over the star rating will display the numeric value of the rating.

A Poems link can also be clicked to display all poems.

## Poems
Displays all poems generated for a café, along with their inspiration and date created. Ordered by most recently created.

### Description of files

Non-Python files:

| filename                           | description                                                                                                                                                               |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| README.md                          | Text file (markdown format) description of the project.                                                                                                                   |
| requirements.txt                   | Text file of packages to be installed by pip.                                                                                                                             |
| .env.example                       | Text file for API keys to be populated and renamed.                                                                                                                       |
| coffee/static/coffee/cafe.js       | Javascript file. Contains most of the review and edit logic. Updates stars and ratings and re displays them after saving. <br/>Displays changed description after saving. |
| coffee/static/coffee/styles.css    | Css file with shared styling for the project.                                                                                                                             |
| coffee/static/coffee/tooltips.js   | Javascript file. Enables bootstrap tooltips.                                                                                                                              |
| coffee/static/coffee/validation.js | Javascript file to apply form validation                                                                                                                                  |

HTML files in the templates/coffee folder:

| filename                        | description                                                                                                                                                               |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cafe.html                       | Displays a single café. All pictures of the cafè are shown via a carousel. A cafès details can be edited, a cafè can be reviewed and there is a link to historical poems. |
| index.html                      | Displays all cafè's to all users. Allows a cafè to be selected.                                                                                                           |
| layout.html                     | Shared structure for the project. Loads css styling and javascript. Contains the NavBar.                                                                                  |
| login.html                      | Displays login page when "Log In" selected from the NavBar.                                                                                                               |
| my_cafes.html                   | Displays logged in users cafè's when "<User>'s Cafès" selected from the NavBar. Allows a cafè to be selected.                                                             |
| new.html                        | Allows the creation of a new cafè when "New" selected from the NavBar. Only visible if user logged in.                                                                    |
| poetry.html                     | Displays historical poems for a café.                                                                                                                                     |
| register.html                   | Displays create new user page when "Register" selected from the NavBar.                                                                                                   |
| includes/edit.html              | Modal to edit a cafés description and add additional images. Used in cafe.html                                                                                            |
| includes/list_display_card.html | Card to display a cafè details with a photo. Used in index.html and my_cafes.html                                                                                         |
| includes/poem_display_card.html | Card to display a haiku, its inspiration and its date created. Used in poetry.html                                                                                        |
| includes/review.html            | Allow user to review a cafè. Used in cafe.html                                                                                                                            |
| includes/star_rating.html       | Display star rating. Used in cafe.html                                                                                                                                    |

Python modules:

| filename  | description                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| admin.py  | Classes for Model Administration. Entries allow models to be updated via django admin                                                                                                                           |
| ai.py     | Functions for interacting with openai, and cleaning content received                                                                                                                                            |
| apps.py   | Standard AppConfig class for application                                                                                                                                                                        |
| forms.py  | Classes for form entry                                                                                                                                                                                          |
| models.py | Model Classes. Has entries for the following models: User, Cafe, Image, Review, CoffeeDescription & Poem                                                                                                        |
| urls.py   | Url routes for all views                                                                                                                                                                                        |
| utils.py  | Utility functions called by views                                                                                                                                                                               |
| views.py  | Views rendering html templates CoffeePoetryView, MyCafesView , cafe_view , new_cafe , login_view, logout_view, register, poetry_view <br/> and views returning json: rating_view, haiku_view,  save_edited_view |

