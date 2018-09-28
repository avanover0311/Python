from flask import Flask, render_template  
app = Flask(__name__)    
                                   
                                                  
@app.route('/play')
def plop():
	return render_template('index.html')                            

@app.route('/play/<num>')
def play(num):
	return render_template('index.html', times=int(num)) 

@app.route('/play/<num>/<color>')
def plast(num,color):
	return render_template('index.html', times=int(num), color=color) 


app.run(debug=True) 