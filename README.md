### Coffee Poetry
A website which allows one to add and review coffee shops, and then generates a poem 
for a coffee shop based on its description and adjectives provided

Only the user who created a cafe can edit it 

## Technologies

## Setup
`code`

## Run
`python manage.py runserver`

## Distinctiveness and Complexity
The website is distinctive as it's main use is to review and advertise coffee shops.
This is done using a traditional review system, along with a creative, changing component - the Poetry generation 
part of the website which is there to encourage users to return more frequently

The complexity comes from incorporating the review system along with the AI generation of a poem which will be 
refreshed every time a coffee shops text or adjectives change. The project also uses testing more than any of the 
previous projects - could put more here depending on test coverage obtained (perhaps a coverage html report?) 
Images - Allow the uploading of multiple images


## File Descriptions
*** coffee/models.py ***
Contains models for User (inherited from AbstractUser), CoffeeShop, Review, Adjective, Poems

coffee/static/coffee/styles.css
Shared styling for the project

templates/coffee/create.html
templates/coffee/index.html
templates/coffee/layout.html
templates/coffee/login.html
templates/coffee/register.html

coffee/tests.py
coffee/urls.py
coffee/views.py
