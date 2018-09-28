from flask import Flask  
app = Flask(__name__)    
                         
print(__name__)          
@app.route('/')          
                          
                         
def hello_world():
    return 'Hello World!'  
                              
@app.route('/dojo')
def dojo():
	return 'Dojo!'

@app.route('/say/<name>')
def flask(name):
	print (name,1)
	return 'Hi ' +name

@app.route('/say/<name>')
def micheal(name):
	print (name,2)
	return 'Hi ' + name

@app.route('/say/<name>')
def john(name):
	print (name,3)
	return 'Hi ' + name

@app.route('/repeat/<num>/<name>')
def hello(num, name):
	print (hello)
	return 'hello '* int(num)
	
@app.route('/repeat/<num>/<name>')
def dogs(num, name):
	print (dogs)
	return ('dogs '* int(num))

app.run(debug=True) 