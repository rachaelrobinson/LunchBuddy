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
        # TODO: gather all info and add to db
        # what data do you want and how?
        # if successful add to DB:
        return jsonify([{'status':200}])
    # similar format to register
    # __name__
    # campus options
    # schedule

@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        session['user'] = ""
        session['logged_in'] = False
        return redirect(url_for('home'))

@app.route('/profile/{username}')
def profile(username):
    if not session.get('logged_in') or not session.get('user'):
        return redirect(url_for('home'))
    if session.get('user') != username:
        return redirect(url_for('home'))
    #display info from registration db, along w/ scheduled dates
    # username is just email
    pass

@app.route('/lunchform', methods=['POST'])
def lunchImport():
    if 'campus' in request.form and 'bday' in request.form and 'ptime' in request.form and 'stime' in request.form:
        primaryid = request.form['campus'] + request.form["bday"] + request.form["ptime"]
        secondaryid = request.form['campus'] + request.form["bday"] + request.form["stime"]

        primaryentry = mongo1.db.find_one({"_id": primaryid})
        if (primaryentry is None):
            primarydate = {"_id" : primaryid, "users" : [session['user']]}
            mongo1.db.primary_time.insert_one(data)
        else:
            primaryentry['users'].append(session['user'])
            mongo1.db.primary_time.update_one(data)

        secondarydate = {"_id" : secondaryid, "users" : [session['user']]}
        if (secondarydate is None):
            primarydate = {"_id" : secondaryid, "users" : [session['user']]}
            mongo1.db.primary_time.insert_one(data)
        else:
            primaryentry['users'].append(session['user'])
            mongo1.db.primary_time.update_one(data)

        return jsonify([{'status':200}])
    else:
        flash('Missing fields!')
        return jsonify([{'status':400}])

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000, threaded=True)

