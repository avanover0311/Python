# import Flask
from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    return render_template("formval.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['name']) <= 3:
        flash("Name must be 3+ characters", 'name')
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!", 'comment')
    elif len(request.form['comment']) <= 10:
        flash("Comment must be 10 characters or less", 'comment')
    if len(request.form['location']) < 0:
    	flash("you forgot location")
    if len(request.form['language']) < 0:
    	flash("you forgot language")
    print(request.form)
    session['name']= request.form['name']
    session['location']=request.form['location']
    session['language'] =request.form['language']
    session['comment'] = request.form['comment']
    if '_flashes' in session.keys():
        return redirect("/")
    else:

        return redirect('/success')

@app.route("/success")
def success():
	return render_template('success.html')


if __name__=="__main__":
    app.run(debug=True)