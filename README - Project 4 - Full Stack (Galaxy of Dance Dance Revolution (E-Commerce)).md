# Project's Name : Galaxy of Dance Dance Revolution
https://roczi-danceapp.herokuapp.com
https://github.com/RocZi/full-stack-assignment4-danceapp3

>> Assignment4-Full Stack Frameworks with Django Milestone Project
My project is called "Galaxy of Dance Dance Revolution". It is an E-commerce web application that sells dance gear and products targetting at every person who dances, either as an amateur or professionally and even cater for gamers who like to play dancing game in the comfor of their home.

We also provide tailor services for whoever wish to make any bulk orders.


## UX

This web application is for user to purchase their dance gear and accessories, and to contact the company for tailor services. From the home page, users will see the company logo and a welcome text.

There is a search bar in every page and right in the beginning home page, they can straightaway search for a name of the product they are looking for.

As a user who wants to purchase individual dance gear and accessories, they can go to the products page to view the different type of products available, view the price per item, key in the amount that they wish to buy for each item and click Add to include the item and amount to Cart. The minimum default number of item to add is 1 and only 1 item and its amount can be added at a time.

As a user who wants to make bulk purchases of dance gear and accessories for recital, dance productions, group performances, we allow each product to be purchase up till 999 per click of add, to include to cart. They can add beyond 999 of the same item by inserting a new figure and clicking a second time of the 'add' button to cart, and so on and so forth. The same item in the cart will be updated with the new total amount of items and the total price. They can then browse the other products to do the same.

As a user who is looking for tailor services for custom made costumes, they can contact the company directly with the contact info prodived in the home page. Users will be able to see a bright red text update if the company has been fully booked with their tailor services orders, along with an indication of when the company will be free to take in new orders again.

With items in the cart, all above users can click cart to view all the items they have chosen, the amount of items they have keyed in altogether, and the total price for each item as well as for all items at the bottom of the page. From this cart page, should they wish to amend the amount, they can key in a new number for and click Amend to change the number. Only 1 item can be amended at a time.

When its time to click Checkout at the cart page to make payment, the web application will check whether the user has already signed in. If not, the user will be brought to the login page where they have to key in their username and password. If they forgotten their password, they can use the Forgot Password link which will bring them to the reset password page. Else they can click on Register to create an account and password.

Once a user is able to login, there will be a confirmation message appearing on top and the Profile text in the navbar will replace the Register text and clicking on it will show user details (as of this web app, it says who is logged in). Furthermore, they can now click Checkout at Cart page and it will show them once again the products they have chosen, amount of items per product, the total price and the payment form where the user key in their particulars and their credit card details.

The user then can click submit to make a purchase and a message will appear on top to indicate whether payment is successful or not.

The user can click logout at any time to log off. There will be a confirmation message appearing on top.


## Features
### Existing Features
- Feature 1 - when a user first gets into the home page, there will be a search bar visible on top after the logo brand picture. This search bar function is also visible and available in every webpage to allow user to search products at any time

- Feature 2 - allows user to view all products and information pertaining to each product, eg. the picture, name, description and price per product, and add products to the Cart by keying in the amount of items per product

- Feature 3 - allows user to view the Cart to see all the products chosen, the amount of items per product that the user keyed in, and the total price of all the products and its amount of items chosen

- Feature 4 - allows user to register for a new user account with username, email address, password and password confirmation

- Feature 5 - allows user to login if they already have an account registered successfully and have their own profile page

- Feature 6 - allows user to reset their password if are unable to login. by sending an email to email address they keyed in

- Feature 7 - allows user to logout at anytime if they wish to, after logging in

- Feature 8 - allows user to make payment after clicking Checkout at the Cart page and then submitting the personal particulars and credit card details

- Feature 9 - allows superuser with admin privileges to go into the admin panel to 
    > create new products, new users, upload new product pictures, 
    > view current orders in the cart, current users, login status, user personal info, product info
    > modify details of products, users, orders,
    > delete products, users, orders,

    Superuser Account login
    https://roczi-danceapp.herokuapp.com/admin
    username : superuser
    password : asdf1324


### Features Left to Implement
Feature ideas would be :
- to fill up user personal particulars at the checkout page if a user is already logged in 
- allow user to sell their own products by filling up a form and uploading their product picture
- allow search with multipe words
- allow cart to remember each user last total added products but not yet purchased so user can continue shopping
- messages to appear when products added
- payment to display messages when payment form not fully completed and submit is pressed


## Technologies Used
- Python : The programming language used for this backend project

- Django : The Python framework used to route urls and for the database

- Jinja2 : The Python Template Engine used to display data from gathered by python onto html

- Bootstrap (getbootstrap.com) : Bootstrap is used to enable mobile responsive webpages

- jQuery (jquery.com) : jQuery is used to simplify DOM manipulation, which is also used in stripe and in bootstrap themselves

- Canva (www.canva.com) : Canva was used to design and create the website logo



## Testing
I did manual testing as follows :
1. Home:
    1. Go to the url "https://roczi-danceapp.herokuapp.com"
    2. verified that correct html loaded with logo seen with welcome text, address, contact info and tailor services, as well as search bar is visible

2. Products:
    1. Click on the "Products" link on nav bar and verified that the page reloads to the correct html showing all the products I have added from admin panel
    2. navbar and search bar is visible
    3. Verified that each product has a number input field and increment / decrement arrow to press to increase or decrease item.
    4. Verified that clicking add at each product made the page reloads correctly back to products page and the Cart at the navbar to display a number, which is the number of item of the product that I keyed in the number and clicked Add.
    5. Verified that the number at the Cart updates correctly as per number of items keyed in per product, as I click add at every product

3. Cart:
    1. This is for non-login status with Register and Login appearing at navbar
    2. after doing the tests at no. 2. Products, verified that clicking Cart will go into the correct html
    3. verified that all the products that I have just added is correct and the number of items per product is correct as well, and the total price is correct as well
    
4. Register:
    1. Click on "Register" at navbar and verified that correct html loaded with form to be inputted and navbar and search bar is visible
    2. Check username, email, password and password confirmation fields are required and verified that I can't continue unless all these are keyed in
    3. try to key in invalid character at username and message appears to request to enter valid username
    4. try to key in invalid email and message appears to request to enter valid email
    5. try to key in different passwords and message appears to say passwords do not match
    6. refill everything with correct and valid input and click on "Create Account" button
    7. verified page reloads and message appears on top "You have successfully registered"
    8. Go to "https://roczi-danceapp.herokuapp.com/admin/auth/user/" page, login as superuser, to check and verified that user appeared in the list
    9. Also tested the "Already got an account? Sign In" link and verified that page loads to the correct html

5. Profile:
    1. While still logged in, click on "Profile" and verified that correct html page loads and navbar and search bar is visible
    2. Verified that email shown is the correct email as per the username that i am logged into

6. Log Out:
    1. Click on "Log Out" at navbar and verified that correct products html page loads and navbar and search bar is visible
    2. Verified that message on top says "You have successfully logged out"
    3. Verified that number beside Cart at navbar has disappeared
    4. Clicking on "Cart" now shows that cart is now empty and total price is $0, which is intended as the user has logged out.
    
7. Log In:
    1. Click on "Log In" at navbar and verified that correct html page loads and navbar and search bar is visible
    2. try to login without username / email and password and verified that both fields must be filled
    3. try to login with correct username and correct password and verified that I can log in
    4. try to login with correct email and correct password and verified that I can log in
    5. try to login with correct email and wrong password and verified that I cannot log in and message appaers "Your username or password are incorrect"
    6. try to login with correct username and wrong password and verified that I cannot log in and message appaers "Your username or password are incorrect"
    7. try to login with wrong username and valid password and verified that I cannot log in and message appaers "Your username or password are incorrect"
    8. try to login with wrong email and valid password and verified that I cannot log in and message appaers "Your username or password are incorrect"

8. Forgot Password:
    1. While at Log In page, click on "Forgot Password" and verified that correct html page loads and navbar and search bar is visible
    2. try to key in invalid email and verified that field must be filled correctly
    3. try to key in valid email type, and verified that message appears "We've e-mailed you instructions for setting your password to the e-mail address you submitted. You should be receiving it shortly."

9. Amend:
    1. While Logged In, with products added to cart, click on "Cart" at navbar and verified correct html page loads and navbar and search bar is visible
    2. verified that products chosen is correct and the current in cart numbers are correct
    3. try to amend by key in a number different from the current number and verified that the current number and the price will update correctly

10. Checkout:
    1. While Logged In, with products added to cart, click on "Checkout" at Cart page and verified correct html page loads and navbar and search bar is visible
    2. verified that products chosen, total quantity numbers and total price are correct
    3. try to not key in anything and verified all fields are required except postal code and the credit card form. clicking submit doesn't do anything. as mentioned in features to implement, more messages are required to let the user know what is going on and what is the required action and input from the user
    4. test keying in correct credit card details and fill in a 6 digit postal code and press submit and verified message appears "You have successfully paid"
    5. Go to my stripe account to check the dashboard and verified that the transaction number increases and the total price is increased correctly. Pls see this picture for my stripe dashboard https://ibb.co/0DPB0wJ

11. Different Browsers:
    1. Each web page looks equally good in desktop Chrome, Firefox, Internet Explorer and Edge
    2. internet explorer shows distortion at homepage
    3. Mobile browser chrome checked and working well
    4. Using Developer Tools in desktop chrome, the default variety of phone and tablets dimensions given are used to check on mobile browsers and all seems well
    5. Desktop Firefox display navbar icons differently from Desktop Chrome

On my manual testing :
One way to see my testing logs is based on the current data in the database. If you go to http://backend-assignment3-roczi.c9users.io:8080/movies_admin (I am using Desktop Chrome) and press Ctrl+F and type in "None", all the "None" will be highlighted and as you scroll down, you would see that the amount of "None" per record reduces as I code the relations correctly and retrieve and display the data correctly, as per their increasing ids for each columns.

However, Bugs:
- Was told switching from cloud9 phpmyadmin to removesql is necessary for heroku deployment. Filter By function does not work using remotesql
- got the error pymysql.err.InternalError: (1055
- if i change my code not to use GROUP BY, i get error pymysql.err.InternalError: (1140
- after trying a few online solutions to disable sql_mode=only_full_group_by, it is still not working
- sample filter including count that is success using cloud9 phpmyadmin : https://ibb.co/X3RZPnt
- can swith the connection back to cloud9 localhost, restart the app, to use the filter by function.


## Deployment
- I make use of the guide and steps given by Code Institute online Learning Materials
DEPLOYING DJANGO ON HEROKU

Install the following using pip3:

sudo pip3 install gunicorn
sudo pip3 install psycopg2
sudo pip3 install whitenoise

Add Whitenoise to the middleware inside settings.py
MIDDLEWARE = [
.....
'whitenoise.middleware.WhiteNoiseMiddleware',
]

Make sure to include the following settings for static files and uploads, if they are not there already:



STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CREATE these folders at workspace level
Static, media and staticfiles
Put empty files inside like test.txt or empty.txt


Create a static folder in the workspace (where manage.py is) and create an empty text file inside there.

Create a staticfiles folder in the workspace and create an empty text file inside there

Create a media folder in the workspace and create an empty text file inside there.

Remove media/ from the .gitignore file temporarily. 

Create the requirements.txt file using bash

pip3 freeze --local > requirements.txt


Create a local git repo for your project and connect it to a GitHub repo. Include the relevant .gitignore file. 

sudo git init 
sudo git add .
sudo git commit -m "First commit"
sudo git remote add origin <GITHUB REMOTE URL> https://github.com/RocZi/full-stack-assignment4-danceapp3
sudo git push origin master

Put back media/ inside .gitignore

Log into heroku by typing in heroku login and pressing ENTER

Create an app

heroku create <PROJECT NAME> roczi-danceapp

git remote -v

ADDING POSTGRES SQL

Type in:
heroku addons:create heroku-postgresql

Install with pip3:
sudo pip3 install dj_database_url

Check the url of the database:
heroku config

Go settings.py, comment out the DATABASES section
Add the URL to the database configurations inside settings.py

import dj_database_url

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

THEN COPY AND PASTE THE WHOLE postgres link as a STRING
DATABASES = {'default': dj_database_url.parse("<long link from heroku website>”)}

I put all the sensitive data and links  into env.py file and settings.py to link to env.py:
os.environ.setdefault("STRIPE_PUBLISHABLE", "")
os.environ.setdefault("STRIPE_SECRET", "")
os.environ.setdefault("DATABASE_URL", "")
os.environ.setdefault("SECRET_KEY", "")
os.environ.setdefault("AWS_SECRET_KEY_ID", "")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")


Migrate and create the superuser

python3 manage.py migrate
heroku run python manage.py createsuperuser

	
DEPLOYING
Commit the changed files

sudo pip3 freeze --local
sudo git add .
git commit -m "<YOUR COMMENT MESSAGE>"
git push origin master

Create the Procfile:

touch Procfile
And enter into the Procfile:

web: gunicorn <PROJECT_FOLDER>.wsgi:application
Eg. web: gunicorn dance_project.wsgi:application (name of the project folder where settings.py, urls.py wsgi.py are)

Add the URL of the heroku app into the ALLOWED_HOST inside settings.py

Add and commit

sudo git add .
sudo git push heroku 

later i go to Heroku website and connect my heroku app to github directly
from this on, i do not need to git push from cloud 9 to heroku
i just git push to github 
and then go to heroku website and deploy from there
i just have to make sure i commented out import env from settings.py or else heroku app will not open

then I re-run the app in cloud 9 terminal and my app is able to be opened from heroku.


## Credits
- Code Institute online Learning Materials
- google and stackoverflow for lots of troubleshooting


### Content
- text content for products description, product names, homepage welcome text are all self created


### Media
- pictures are all search via google images for keywords
- logo is created via www.canva.com


### Acknowledgements

- I received inspiration for this project from having friends in the dance industry whom sells dance products online
