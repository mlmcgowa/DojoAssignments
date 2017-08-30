from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'hogs4647'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_reg')

@app.route('/')
def index():

    if 'x' not in session:
        session['x'] = 0
        session['firsttime'] = True
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def checker():

    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)

    if len(user) > 0:

        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            session['x'] = user[0]['id']
            session['firsttime'] = False
            return redirect('/welcome')

        else:
            flash("Incorrect password!")
            return redirect('/')
    else:
        flash("Please Register!")
        return redirect('/register')

@app.route('/welcome')
def success():

    query = "SELECT * FROM users WHERE id = :specific_id"
    data = {'specific_id': session['x']}
    user = mysql.query_db(query, data)
    return render_template('success.html', specific_user=user[0])

@app.route('/register')
def showRegister():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():

    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']
    pw = request.form['pword']
    cpw = request.form['c-pword']
    valid_status = True

    if len(fname) < 2:
        valid_status = False
        flash("First name has to be more than 2 characters!", 'error')

    if re.search(r'[0-9]', fname):
        valid_status = False
        flash("First name cannot contain numbers!", 'error')

    if len(lname) < 2:
        valid_status = False
        flash("Last name has to be more than 2 characters!", 'error')

    if re.search(r'[0-9]', lname):
        valid_status = False
        flash("Last name cannot contain numbers!", 'error')

    if not re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
        valid_status = False
        flash("Invalid E-mail format!", 'error')

    if len(pw) < 8:
        valid_status = False
        flash("Password should be at least 8 characters!", 'error')

    if pw != cpw:
        valid_status = False
        flash("Passwords do not match!", 'error')

    if valid_status:
        pw_hash = bcrypt.generate_password_hash(pw)
        insert_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:fname, :lname, :email, :pw_hash, NOW(), NOW())"
        query_data = {'fname': fname, 'lname': lname, 'email': email, 'pw_hash': pw_hash}
        mysql.query_db(insert_query, query_data)

        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user = mysql.query_db(user_query, query_data)
        session['x'] = user[0]['id']
        return redirect('/welcome')

    else:
        return redirect('/register')

@app.route('/logout', methods=['POST'])
def logMeOut():

    session.pop('x')
    return redirect('/')

app.run(debug=True)
