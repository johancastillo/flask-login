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

# Route Main
@app.route("/")
def Main():
    if "name" in session:
        return render_template("index.html")
    else:
        return render_template("login.html")

# Route Home
@app.route("/home")
def Home():
    if "name" in session:
        return render_template("index.html")
    else:
        return render_template("login.html")


# Route Register
@app.route("/register", methods=["GET", "POST"])
def Register():
    if(request.method == 'GET'):
        # Access Denegade
        return render_template("login.html")
    else:
        # Get data
        name = request.form['nameRegister']
        email = request.form['emailRegister']
        password = request.form['passwordRegister']

        password_encode = password.encode("utf-8")
        encrypted_password = bcrypt.hashpw(password_encode, seed)
        print("Insertado:")
        print("Password encode: ", password_encode)
        print("Password encypted: ", encrypted_password)

        # Prepare Query for insertion
        sQuery = "INSERT INTO login (name, email, password) VALUES (%s, %s, %s)"

        # Creating cursor for execute
        cursor = mysql.connection.cursor()

        # Execute sentence
        cursor.execute(sQuery, (name, email, password))

        # Execute commit
        mysql.connection.commit()

        # Register sesion
        session['name'] = name
        session['email'] = email

        # Redection to Index
        return redirect(url_for('Home'))


# Route Login
@app.route("/login", methods = ["GET", "POST"])
def Login():
    if(request.method == "GET"):
        if 'name' in session:
            # Load template main
            return render_template("index.html")
        else:
            # Access Denegade
            return render_template("login.html")
    else:
        # Get data
        email = request.form['emailLogin']
        password = request.form['passwordLogin']
        password_encode = password.encode("utf-8")

        # Creating cursor
        cursor = mysql.connection.cursor()

        # Prepare Query
        sQuery = "SELECT name, email, password FROM login WHERE email = %s"

        # Execute sentence
        cursor.execute(sQuery, [email])

        # Get data
        user = cursor.fetchone()

        # Close consultation
        cursor.close()

        # Verification
        if(user != None):
            # Get password
            password_encryptoded_encode = user[1].encode
            


# Run server
app.run(port = 8080, debug = True)

