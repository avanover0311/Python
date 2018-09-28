from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__) 
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('emailval')
app.secret_key = 'secrets' 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')  
def index():
    return render_template("Email_Val.html")


@app.route('/process', methods=['POST'])
def process():
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
			return redirect("/")
	return ('Success!')	

app.run(debug=True)    