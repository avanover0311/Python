from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__) 
app.secret_key = 'secrets'
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('registration')
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')  
def index():
    return render_template("registrationvalid.html")


@app.route('/process', methods=['POST'])
def process():
	if len(request.form.get('first_name', "")) < 2:
		flash ('Needs first name!')
	else:
		flash("Success! Your name is " + request.form['first_name'])

	if len(request.form.get('last_name', "")) < 2:
		flash ('Needs last name!')
	else:
		flash("Success! Your name is " + request.form['last_name'])

	if len(request.form.get('password', "")) < 8:
		flash ('Needs at least 8 characters!')
	else:
		flash("Success! You have a password!")
		
	if len(request.form.get('email', "")) < 1:
		flash ('Needs email!')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email!")
		return redirect('/')
	else:
		query = "SELECT * FROM email WHERE email (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
		data = {'email': request.form['email']}
		results = mysql.query_db(query, data)
		if results:
			flash("email already exists!")	
			return redirect('/')
	return ('Success!')

def passcheck():
	if len(request.form.get('password', "")) < 8:
		flash ('Invalid Password! Must have at least 8 characters')
	if request.form.get('password') != request.form.get('verifypass'):
		flash ('Password Confirmation does not match Password!')
	return render_template("registration.html")





app.run(debug=True)    