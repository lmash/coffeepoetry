# Coffee Poetry
The idea behind the website is for coffee to inspire poetry.
The website allows one to add and review a café, and then generates a poem 
based on the café and coffee descriptions provided.

## Poetry Generation
- Poetry generation runs after each review is entered
- Only cafés with an average rating of 4.2 or higher and 3 or more review descriptions can generate poetry
- The AI uses a combination of the café and coffee descriptions (3 coffee descriptions are randomly selected) to generate a haiku

## Technologies

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

## Distinctiveness and Complexity
The website is distinctive as it's main use is to review and advertise speciality cafès.
This is done using a traditional review system, along with a creative component - the Poetry generation 
part of the website which is there to encourage users to return more frequently, and is only available for the highest rated 
cafès.

The complexity comes from incorporating the review system along with the AI generation of a poem which will be 
refreshed every time a cafè (which qualifies) coffee description changes. The project also uses testing more than any of the 
previous projects - could put more here depending on test coverage obtained (perhaps a coverage html report?) 
Images - Allow the uploading of multiple images. For additional complexity the site has been deployed and is available at www.?????.??? 
Migrations also include data migrations as initial data

### File structure

```
├── README.md
├── capstone
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── coffee
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── static
│   │   └── coffee
│   │       ├── cafe.js
│   │       ├── styles.css
│   │       └── validation.js
│   ├── templates
│   │   └── coffee
│   │       ├── cafe.html
│   │       ├── includes
│   │       │   ├── list_display_card.html
│   │       │   ├── review.html
│   │       │   └── star_rating.html
│   │       ├── index.html
│   │       ├── layout.html
│   │       ├── login.html
│   │       ├── my_cafes.html
│   │       ├── new.html
│   │       ├── poetry.html
│   │       └── register.html
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_forms.py
│   │   ├── test_models.py
│   │   ├── test_utils.py
│   │   └── test_views.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── manage.py
├── media
│   └── images
│       ├── Hamad_Darwish_Wallpapers_-1.jpg
└── requirements.txt
```
## Description of files

Non-Python files:

| filename             | description                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------|
| README.md            | Text file (markdown format) description of the project.                                                 |
| requirements.txt     | Text file of packages to be installed by pip.                                                           |
| .env.example         | Text file for API keys to be populated and renamed.                                                     |
| coffee/cafe.js       | Javascript file. Contains most of the review logic and  listeners for events, updates stars and ratings |
| coffee/styles.css    | Css file with shared styling for the project.                                                           |
| coffee/validation.js | Javascript file to apply form validation                                                                |

HTML files in the templates/coffee folder:

| filename                        | description                                                                                                                          |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| cafe.html                       | Displays a single cafe. All pictures of the cafè are shown via a carousel. A cafès details can be edited and a cafè can be reviewed. |
| index.html                      | Displays all cafè's to all users. Allows a cafè to be selected.                                                                      |
| layout.html                     | Shared structure for the project. Loads css styling and javascript. Contains the NavBar.                                             |
| login.html                      | Displays login page when "Log In" selected from the NavBar.                                                                          |
| my_cafes.html                   | Displays logged in users cafè's when "<User>'s Cafès" selected from the NavBar. Allows a cafè to be selected.                        |
| new.html                        | Allows the creation of a new cafè when "New" selected from the NavBar. Only visible if user logged in.                               |
| poetry.html                     | T.B.C. when "Poetry" selected from the NavBar. Only visible if user logged in.                                                       |
| register.html                   | Displays create new user page when "Register" selected from the NavBar.                                                              |
| includes/list_display_card.html | Card to display a cafè details with a photo. Used in index.html and my_cafes.html                                                    |
| includes/review.html            | Allow user to review a cafè. Used in cafe.html                                                                                       |
| includes/star_rating.html       | Display star rating. Used in cafe.html                                                                                               |

Python modules:

| filename  | description                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------|
| admin.py  | Classes for Model Administration. Entries allow  models to be updated via django admin           |
| apps.py   | ???                                                                                              |
| forms.py  | Classes for form entry                                                                           |
| models.py | Model Classes. Has entries for the following models: User, Cafe, Image, Review, Adjective & Poem |
| urls.py   | ???                                                                                              |
| utils.py  | Classes for Model Administration. Entries allow  models to be updated via django admin           |
| views.py  | ???                                                                                              |

