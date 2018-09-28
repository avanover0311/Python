from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'ThisIsSecrethjnkjn'

@app.route('/')
def index():
	session['num'] = int(1)
	return render_template("counter.html")

@app.route('/count', methods=["POST"])
def count_user():
	session['num'] = session['num'] + int(2)

	return render_template("counter.html")

@app.route('/reset', methods=["POST"])
def reset():
	session['num'] = int(0)
	return redirect('/')


app.run(debug=True)

