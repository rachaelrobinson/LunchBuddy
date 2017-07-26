from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for
from flask_pymongo import PyMongo
from flask_mail import Message, Mail
import os
app = Flask(__name__)
with app.app_context():
    mongo1 = PyMongo(app)
    app.config['MONGO_DBNAME'] = 'users'
    app.config['MONGO2_DBNAME'] = 'timeslots'
    mongo2 = PyMongo(app, config_prefix='MONGO2')
mail = Mail()
"""
Region:
W - (Redmond-West)
E - (Redmond-East)
B - (Bellevue)
N - (North)
Time:
0 - 11 -> 12
1 - 12 -> 1
2 - 1 -> 2
Doc schema
"_id": {Region}-{Time} (primary)
"name": name
"secondary-options": [{Region}{Times}]
"""
# @app.route('/dbtest')
# def db_test():
# 	post = {"_id": 'W1',
# 		"name": 'Leela',
# 		"sec_opt":['W2', 'E1']}
# 	mongo1.db.test.insert_one(post)
# 	return 'made it'

@app.route('/dbtest')
def db_test():
    # post = {"_id": 'W-12/1-1',
    # 	"name": 'Leela',
    # 	"sec_opt":['W2', 'E1']}
    # result = mongo1.db.users.insert_one(post)
    post2 = {"_id": 'test2',
             "name": 'temp',
             "reg": 'w3'}
    result2 = mongo2.db.junk.insert_one(post2)
    return result2.inserted_id
    # return 'made it'

@app.route('/')
def home():
    # We should have some option to redirect to /register if they don't have an account
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return redirect(url_for('/reserve'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'password' in request.form and 'username' in request.form:
            print "HERE"
            session['logged_in'] = True
            session['user'] = request.form['username']
            #TODO: Add to database
            print request.form['password']
            print request.form['username']
            
            return jsonify([{'status':200}])
        else:
            flash('password_incorrect!')
            return jsonify([{'status':400}])
    elif request.method == 'GET':
        if session.get('logged_in'):
            return redirect(url_for('reserve'))
        else:
            return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # if not session.get('logged_in'):
        # 	return render_template('login.html')
        if 'name' in request.form and 'email' in request.form and 'password' in request.form:
            print request.form['name']
            print request.form['password']
            print request.form['email']
            data = {"_id": request.form['email'],
                    "name": request.form['name'],
                    "password": request.form['password']}
            # check to see if user already registered, if they are rn it'll over out
            mongo1.db.users.insert_one(data)
            session['user'] = request.form['email']
            # return redirect(url_for('profile'))
            # mongo1.db.test.insert_one(data)
            #TODO: add user to session
            return jsonify([{'status':200}])
        else:
            flash('Missing fields!')
            return jsonify([{'status':400}])
        #name, email, password
    else:
        return render_template('signup.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'GET':
        if session.get('logged_in'):
            return render_template("reserve.html")
        else:
            return render_template('login.html')
        # similar format to register
        # __name__
        # campus options
        # schedule
    else:
        print request.form['date']
        print request.form['pcampus']
        print request.form['stime']
        # Things you get back from form:
            #pcampus: (N, E, W, B)
            #scampus: (N, E, W, B)
            #ptime: (0, 1, 2) 0=11-12, 1=12-1, 2=1-2
            #stime: (0, 1, 2)
            #date: (YYYY-MM-DD)
        # if successful add to DB:
        return jsonify([{'status':200}])
    # similar format to register
    # __name__
    # campus options
    # schedule

@app.route('/logout', methods=['GET'])
def logout():
    if request.method == 'POST':
        session['user'] = ""
        session['logged_in'] = False
        return redirect(url_for('home'))

@app.route('/profile')
def profile():
	print "YA GOT IT"
	#dummy data to test profiles
	email = 'rachael@mcrsft.com'
	# reservations = {{'reservation':{'info':'July 25th, 1-2pm, North Campus', 'status':'scheduled'}}, {'reservation':{'info':'July 30th, 1-2pm, North Campus', 'status':'pending'}}}
	name = 'Rachael_Robinson'
	person = {'name': name, 'email': email}
	print person
	#TODO: send username
	return render_template("profile.html", user=person)
	#display info from registration db, along w/ scheduled dates
	# username is just email
	pass
	# if not session.get('logged_in') or not session.get('user'):
	# 	return redirect(url_for('home'))
	# if session.get('user') != username:
	# 	return redirect(url_for('home'))
	# else:
	# 	print "YA GOT IT"
	# 	#dummy data to test profiles
	# 	email = 'rachael@mcrsft.com'
	# 	reservations = [{reservation:'July 25th, 1-2pm, North Campus', status:'scheduled'}, {reservation:'July 30th, 1-2pm, West Campus', status:'pending'}]
	# 	name = 'rachaelrobinson'
	# 	#TODO: send username
	# 	return render_template("profile.html", email=email, reservations=reservations, name=name)
	# #display info from registration db, along w/ scheduled dates
	# # username is just email
	# pass
@app.route('/about')
def about():
	return render_template("about.html")

def sendEmail(buddies, place, time): 
	#TODO: get all the emails from the buddies
	EmailMessage 
	EmailMessage = request.form['message']
	msg = Message("You've got buddies for lunch!", sender=('The OurHouse Team', 
	'comp120frhj@gmail.com'), recipients=[LandlordEmail])
	msg.html = render_template('Hybrid/stationery-hybrid.html', useremail=UserEmail, emailmessage=EmailMessage, firstname=LandlordFName)
	mail.send(msg)
	return "Sent"

@app.route('/timeslot', methods=['POST'])
def saveTimeslot():
    if 'campus' in request.form and 'bday' in request.form and 'ptime' in request.form:
        # id: {campus}{time}-{date}
        primaryid = '{}{}-{}'.format(request.form['campus'], request.form["ptime"], request.form["bday"])
        primaryentry = mongo1.db.find_one({"_id": primaryid})
        if (primaryentry is None):
            # add document for time/date/location if it doesn't exist
            primarydate = {"_id" : primaryid, "users" : [session['user']]}
            mongo1.db.timeslots.insert_one(data)
        else:
            primaryentry['users'].append(session['user'])
            # update existing document
            mongo1.db.timeslots.update_one(data)

        return jsonify([{'status':200}])
    else:
        flash('Missing fields!')
        return jsonify([{'status':400}])

<<<<<<< HEAD
# def sendEmail(buddies, place, time): 
# 	#TODO: get all the emails from the buddies
		# create an email account for the application and add that to the env 
		# snag all the emails for everyone in the lunch group
		# creat a message and send to everyone telling them when and where their lunch is 

# 	EmailMessage = request.form['message']
# 	msg = Message("You've got buddies for lunch!", sender=('<Title>', 
# 	'<email>'), recipients=[<users emails>])
# 	msg.html = render_template('Hybrid/stationery-hybrid.html', useremail=UserEmail, emailmessage=EmailMessage, firstname=<lunch buddies?>)
# 	mail.send(msg)
# 	return "Sent"
=======
# to be run periodically, not a route call
def matchBuddies(date):
    # go through in each campus + time
    locations = ['W','E','B','N']
    times = ['1','2','3']
    #TODO : improve this nested for loop to only go through documents that exist on the database
    for location in locations:
        for time in times:
            # find an appropriate timeslot in the database
            id = '{}{}-{}'.format(location,time,date)
            timeslot = mongo1.db.timeslots.find_one(id)

            # if document exists, there are people
            if (timeslot is not None):
                # if user is alone in that timeslot, don't group them
                userCount = len(timeslot['users'])
                if (userCount == 1):
                    # TODO: send an email
                    print 'Send email'
                else:
                    users = timeslot['users']
                    # distribute to separate groups                    
                    matchedUsers = distributeUsers(users)
                    
                    # go through each user and insert a meeting containing the list of people
                    for i in range(len(matchedUsers)):
                        data = { '_id' : id, 'users' : matchedUsers[i] }
                        m_id = mongo1.db.meetings.insert_one(data)
                        # update user with the current m_id
                        for username in matchedUsers[i]:
                            user = mongo1.db.users.find_one(username)
                            # set a meeting ID for the associated user and update the database
                            user.m_id = m_id
                            mongo1.db.users.update_one(user)
                
                # TODO: delete previous entry

            # else just continue, not necessary just done for readability
            else:
                continue

def distributeUsers(users):
    matchedUsers = None
    if (userCount % 6 == 0):
        matchedUsers = initUserArr(userCount/6)
    else:
        # +1 since 7 would mean two groups, while 6 would mean one group
        matchedUsers = initUserArr(userCount/6 + 1)
    # distribute each user to appropriate bucket by dividing in 6
    for i in range(len(users)):
        matchedUsers[i % len(matchedUsers)].append(users[i])
    return matchedUsers

def initUserArr(count):
    arr = []
    for i in range(count):
        arr.append([])
    return arr
>>>>>>> a465b002074ce33bfcf65e715637f78568384ef8

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000, threaded=True)

