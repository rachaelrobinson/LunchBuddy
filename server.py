from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_pymongo import PyMongo
import os
app = Flask(__name__)
# with app.app_context():
# 	mongo1 = PyMongo(app)
# 	mongo1.db.createCollection('test')
# 	app.config['MONGO_DBNAME'] = 'test'
# 	app.config['MONGO2_DBNAME'] = 'test_two'
# 	mongo2 = PyMongo(app, config_prefix='MONGO2')

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

@app.route('/')
def home():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	else:
		return "Welcome!"

@app.route('/register')
def register():
	if not session.get('logged_in'):
		return render_template('login.html')
	if 'name' in request.form and 'email' in request.form and 'password' in request.form:
		data = {"_id": request.form['email'],
				"name": request.form['name'],
				"password": request.form['password']}
		return redirect(url_for('login')) 
		# mongo1.db.test.insert_one(data)
	else:
		flash('Missing fields!')
	#name, email, password

@app.route('/reserve')
def reserve():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	# similar format to register
	# __name__
	# campus options
	# schedule
	pass

@app.route('/login', methods=['POST'])
def login():
	if 'password' in request.form and 'username' in request.form:
		session['logged_in'] = True
		session['user'] = request.form['username']
	else:
		flash('password_incorrect!')
	return home()

@app.route('/profile/{username}')
def profile(username):
	if not session.get('logged_in') or not session.get('user'):
		return redirect(url_for('login'))
	if session.get('user') != username:
		return redirect(url_for('login'))
	#display info from registration db, along w/ scheduled dates
	# username is just email
	pass

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=5000, threaded=True)

