from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for
from flask_pymongo import PyMongo
import os
app = Flask(__name__)
with app.app_context():
	mongo1 = PyMongo(app)
	app.config['MONGO_DBNAME'] = 'users'
	app.config['MONGO2_DBNAME'] = 'timeslots'
	mongo2 = PyMongo(app, config_prefix='MONGO2')

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
			session['logged_in'] = True
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
	if request.method == 'GET':
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

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=5000, threaded=True)

