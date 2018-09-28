from flask import Flask, render_template  
app = Flask(__name__)    
                                   
                                                  
@app.route('/')
def nada():
	return render_template('checkerboard.html')                            



app.run(debug=True) 