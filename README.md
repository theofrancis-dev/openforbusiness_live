# Project OpenForBusiness
Capstone project for the CS50 Web Programming with Python and JavaScript
https://cs50.harvard.edu/web/2020/projects/final/capstone/

The intention of this project is to help small bussines to create an online presentation card.
Also, customers can write and rate the business to help others future customers
which business to select.



### Python's Package needed to run this project.

The file requirement.txt contains all necesary packages. Among them **pillow**, and **crispy forms**.
To install the packages: *$[ pipenv install](https://pipenv-fork.readthedocs.io/en/latest/basics.html " pipenv install")*

## Initializing the Database.
The project needs to initialize two tables before starting.

python manage.py loaddata BusinessClasification.json
python manage.py loaddata ColorScheme.json

The data was originallu dumped with the commands:
python manage.py dumpdata sites.BusinessClasification > BusinessClasification.json
python manage.py dumpdata sites.ColorScheme > ColorScheme.json

------------

## App Users
Keep all referent to user register, login, logout, pasword changes and recovery.

## App Sites
The main part of the project. Keep the logic for the cards.

For this project is used Postgree as a database.

#### Models Description
**BusinessClasification** : Hold the possibles clasification for a business.
**Business** Hold the information related to a business.
**PersonFavorite** : Track the user favorites business.
**ColorScheme** : Color Scheme for business's card.
  
  Color scheme used: 
  https://www.w3schools.com/colors/colors_schemes.asp
  color names given by:
  https://chir.ag/projects/name-that-color
  
**BusinessReview** : Keep reviews for business made by users.

#### Other resources used:
  Font Awesome 4.  https://fontawesome.com/v4.7/icons/
  Flaticon https://www.flaticon.com/
  Markup Editor https://markdown-editor.github.io/

#### Files and Directories
&#x1f4c2; __/__

BusinessClasification.json  

&#x1f4c2; openforbusiness
* Pipfile  
* Pipfile.lock  
* README.md  
* requirements.txt  
&#x1f4c2; static

&#x1f4c2; ./openforbusiness

* appsecrets.py  
* BusinessClasification.json  
* ColorScheme.json  
* manage.py  
* &#x1f4c2;media  
* &#x1f4c2;openforbusiness
* &#x1f4c2;sites
* &#x1f4c2;users

&#x1f4c2; ./openforbusiness/openforbusiness

* asgi.py  
* \_\_init__.py  
* settings.py  
* static  
* templates 
* urls.py  
* views.py  
* wsgi.py

&#x1f4c2; ./openforbusiness/openforbusiness/static

css
images
js

&#x1f4c2; ./openforbusiness/openforbusiness/static/css

loginStyles.css  
new_business_style.css  
styles.css

&#x1f4c2; ./openforbusiness/openforbusiness/static/images

* favicon.ico  
* lteo_logo.png

&#x1f4c2; ./openforbusiness/openforbusiness/static/js

* login.js  
* pwdchange.js  
* pwdreset.js  
* signup.js

&#x1f4c2; ./openforbusiness/openforbusiness/templates

&#x1f4c2; openforbusiness

&#x1f4c2; ./openforbusiness/openforbusiness/templates/openforbusiness

* about.html
* contact.html
* layout.html

&#x1f4c2; ./openforbusiness/sites

* admin.py
* forms.py
* [migrations]
* templates
* urls.py
* apps.py
* \_\_init__.py
* models.py
* static
* tests.py
* views.py

&#x1f4c2; ./openforbusiness/sites/migrations

 _Contain all project’s migrations_


&#x1f4c2; ./openforbusiness/sites/static

* images
* js

&#x1f4c2; ./openforbusiness/sites/static/images

* hand_shake.jpg

&#x1f4c2; ./openforbusiness/sites/static/js

* newbusiness.js  	_instant change html page to see results as information is entered._
* newreview.js  	_Track when user click on the star review_
* sites.js			_Allow rating, flipping the card, set favorite_

&#x1f4c2; ./openforbusiness/sites/templates

&#x1f4c2; sites

&#x1f4c2; ./openforbusiness/sites/templates/sites

* audit.html     
* card.html
* index.html   
* newbusiness.html  
* pagination.html   	&#x1f4cc;_django pagination, html fragment to be included in index html_
* reviews.html  
* cardback.html  
* error.html
* icons.html
* listed.html
* new_review.html   
* previewcard.html  
* schemes.html

&#x1f4c2; ./openforbusiness/users:

* admin.py  
* apps.py  
* forms.py  
* \_\_init\_\_.py  
* migrations  
* models.py  
* static  
* templates  
* tests.py  
* urls.py  
* views.py

&#x1f4c2; ./openforbusiness/users/migrations

&#x1f4c2; ./openforbusiness/users/static

&#x1f4c2; ./openforbusiness/users/templates

registration

users

&#x1f4c2; ./openforbusiness/users/templates/registration

* login.html  
* password_change_done.html  
* password_change_form.html  
* password_reset_done.html  
* password_reset_form.html

&#x1f4c2; ./openforbusiness/users/templates/users

* avatars.html  
* profile.html  
* signup.html

&#x1f4c2; ./static

* admin
* css
* images
* js

&#x1f4c2; ./static/admin _django default directory_

* css		
* fonts		
* img
* js

&#x1f4c2; ./static/css

* loginStyles.css
* new_business_style.css  
* styles.css

&#x1f4c2; ./static/images

* favicon.ico
* hand_shake.jpg
* images
* lteo_logo.png
* photo-camera.png

&#x1f4c2; ./static/images/images &#x1f4cc; _In this directory django keep the images upload to the site_


&#x1f4c2; ./static/js

* login.js  
* newbusiness.js  
* newreview.js
* pwdchange.js
* pwdreset.js  
* signup.js
* sites.js


teopinillo Dec, 2021




















 

  