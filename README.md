# /Project Openforbussines
Capstone project for the CS50 Web Programming with Python and JavaScript/

This project will help small bussines to create a web page an a easy way

needs to install crispy_forms
pip install django-crispy-forms


development
06/16/2021 Initilizaling the project, creating the users logging pages
06/25/2021 Creating index page
06/27/2021 Creating login/register pages

superuser: teopinillo
pass: entrance9

users: gabriel, akira, yirian, thomas, victor, elena, john, silvia, andres
pass: entrance
email: @harvard.edu


07/09/2021
 Created the sites app
 designing the first blueprint for sites

 07/24/2021
  Password reset options

08/04/2021
  from django.contrib.auth.decorators import login_required
  @login_requiered
  https://pypi.org/project/django-login-required-middleware/

08/13/2021
error: "GET /accounts/login/?next=/accounts/login/ HTTP/1.1" 302 0
solution: remove, from settings middleware:  
#'login_required.middleware.LoginRequiredMiddleware',


09/02/2021
add field for bussines: 
  facebook, twitter, instagram
  description line 1
  description line 2
  card imagen

  email,, image1, 2 and 3 could be blank

09/10/2021
  Created a model for styles
  This color style were given a name, the color schemegiven by:
  https://www.w3schools.com/colors/colors_schemes.asp
  color names given by:
  https://chir.ag/projects/name-that-color

  to load default color schemes:
  $ python manage.py loaddata sites/fixtures/color_scheme_data.json


  9/21/2021

  Font Awesome 4
  https://fontawesome.com/v4.7/icons/

  9/22/2021
  Problem: The image to upload with the input is not been saved
  mirar:
  https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/
  https://stackoverflow.com/questions/49096239/django-imagefield-not-uploading-the-image


  camera icon
  <div>Icons made by <a href="" title="Kiranshastry">Kiranshastry</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

  10/12/2021
  Implementing 5 star ratings
  will be a integer from 1 to 5

11/2/2021
Coding Favorite

11/6/2021
 Create an audit page for the data and debug

11/13/2021
 Show all curent user business


{% for r in b.getMaxStars %}
                        {% if r <= b.get_rating %}
                            <span class="fa fa-star checked"></span>
                        {% else %}
                            <span class="fa fa-star"></span>
                        {% endif %}                        
                    {% endfor %}
 

  