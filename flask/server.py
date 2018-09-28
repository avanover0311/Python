from flask import Flask, render_template, request, session, redirect, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('customerleads')

@app.route('/')
def index():
    customer_leads = mysql.query_db("SELECT * FROM customer")
    print("Fetched all customers", customer_leads)
    return render_template('leads.html', customer = customer_leads)



if __name__ == "__main__":
	app.run(debug=True)