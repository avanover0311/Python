from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecrethjnkjn'

@app.route('/')
def index():
	return render_template('numbergame.html')

@app.route('/random', methods=["POST"])
def randnumber():
	randnum =random.randrange(0, 101)
	if randnum < 0  

	print()




def reset():
	session.pop('num')
	return redirect('/')

app.run(debug=True)