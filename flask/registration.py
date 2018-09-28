from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__) 
app.secret_key = 'secrets' 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')  
def index():
    return render_template("registration.html")


@app.route('/process', methods=['POST'])
def process():
	if len(request.form.get('first_name', "")) < 1:
		flash ('Needs first name!')
	else:
		flash("Success! Your name is " + request.form['first_name'])

	if len(request.form.get('last_name', "")) < 1:
		flash ('Needs last name!')
	else:
		flash("Success! Your name is " + request.form['last_name'])

	if len(request.form.get('email', "")) < 1:
		flash ('Needs email!')
	else:
		flash("Success! Your email is " + request.form['email'])

	if len(request.form.get('password', "")) < 1:
		flash ('Needs a password!')
	else:
		flash("Success! You have a password!")
	return redirect('/')

def passcheck():
	if len(request.form.get('password', "")) < 8:
		flash ('Invalid Password! Must have at least 8 characters')
	if request.form.get('password') != request.form.get('verifypass'):
		flash ('Password Confirmation does not match Password!')
	return render_template("registration.html")





app.run(debug=True)    