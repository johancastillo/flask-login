# Imports modules for project
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import bcrypt

# Creating object Flask
app = Flask(__name__)

# Key secrect
app.secret_key = "appLogin"

# Settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jcjohan'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_login'

# Creating object MySQL
mysql = MySQL(app)

# Seed encryption
seed = bcrypt.gensalt()

# Route root
@app.route("/")
def main():
    return render_template("index.html")



# Run server
app.run(port = 8080, debug = True)

