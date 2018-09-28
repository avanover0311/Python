from flask import Flask, render_template, request, session, redirect, flash
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecrethjnkjn'

@app.route('/')
def index():
	session.clear()
	if 'gold' not in session:
		session['gold'] = 0
	if 'activities' not in session:
		session['activities'] = []
	return render_template('ninjagold.html')

@app.route('/process_money/', methods=['POST'])
def money():
	print(request.form)
	if 'farm' in request.form:
		earned_gold = random.randint(10,20)
		session['gold'] += earned_gold
		d ={
		'col': 'green',
		'msg': 'Earned' + str(earned_gold) + " gold from the farm!" + datetime.now().strftime('%Y/%m/%d %i:%M%p')
		}
		session['activities'].append(d)
	elif 'cave' in request.form:
		earned_gold = random.randint(5,10)
		session['gold'] += earned_gold
		d ={
		'col': 'green',
		'msg': 'Earned' + str(earned_gold) + "  gold from the cave!"
		}
		session['activities'].append(d)
	elif 'house' in request.form:
		earned_gold = random.randint(2,5)
		session['gold'] += earned_gold
		d ={
		'col': 'green',
		'msg': 'Earned' + str(earned_gold) + "  gold from the house!"
		}
		session['activities'].append(d)
	elif 'casino' in request.form:
		earned_gold = random.randint(-50,50)
		session['gold'] += earned_gold
		d ={
		'col': 'green',
		'msg': 'Earned' + str(earned_gold) + "  gold from the casino!"
		}
		session['activities'].append(d)
	return redirect('/')

def reset():
	return redirect('/')

if __name__=="__main__":
	app.run(debug=True)








