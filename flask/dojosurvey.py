from flask import Flask, render_template  
app = Flask(__name__)    
                                   
                                                  
@app.route('/')
def index():
	return render_template('dojosurvey.html')                            

@app.route('/results', methods=['POST'])
def result():
	
	print(request.form['first_name'])
	print(request.form['email'])
	email = request.form['email']
	return render_template('results.html', name=request.form['first_name'], t_email=email)


app.run(debug=True)