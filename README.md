# LunchBuddy

Meeting new people for lunch has never been this easy!

##Welcome to LunchBuddy
Lunch Buddy is a Flask web application created during Microsoft's OneWeek Hackathon. This web app is intended to help both new employees and and existing ones meet new people. Employees can sign up for an account with their Microsoft email. Once an employee has a profile, they can fill out a form with the date they would like to go out to lunch, their preferred and secondary times, and their top 3 choices for which campus they would like to eat on. Once that's done, LunchBuddy puts together groups of people and alerts them which group they are in and how to get in contact with each other. 

### Getting started
Note: This project is done using Python 2.7.13

1. Clone the repository

2. To ensure that you have the correct version of Python, we recommend you use a virtual environment. To do so, install virtualenv by running `pip install virtualenv` in the root directory of the application. Once virtualenv has been successfully installed, run `virtualenv venv`. Although this is not 100% neccessary.

3. Ensure that Python 2.7.13 is the version of Python within the virtual environment. 

4. To start up the virtual environment, run `. venv/bin/activate`.  You will need to have your virtual environment running for the entirety of configuring and running this application.  If you see a little (venv) icon next to your user in your terminal, then your virtual environment is running, example:

    (venv) Foo-MacBook-Pro-5:MyFolder Foo$

4b. To install the necessary dependencies, while your venv is running, locate the file requirements.txt, and run `pip install -r requirements.txt`. This will deploy to localhost :5000.

5. This application uses MongodDB as the database. To start a MongoDB server locally using homebrew, open an instance of terminal and run `brew services start mongodb` and then run `mongo`. 

5. To start the app locally, open another instance of terminal and run `python server.py`. 

Notes:

### Packages, APIs, Dependencies
Python 2.7.13 <br />
blinker==1.4 <br/>
click==6.7 <br/>
Flask==0.12.2 <br/>
Flask-Mail==0.9.1 <br/>
Flask-PyMongo==0.5.1 <br/>
itsdangerous==0.24 <br/>
Jinja2==2.9.6 <br/>
MarkupSafe==1.0 <br/>
pymongo==3.4.0 <br/>
Werkzeug==0.12.2 <br/>
=======
