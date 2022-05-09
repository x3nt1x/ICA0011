"""
Database-driven website using Flask & MySQL.
Using GitHub repository and GitHub Actions deploy website to Heroku and migrate local database to ClearDB MySQL.

NOTE: use push_changes.sh to commit changes to GitHub and Heroku!
"""
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

if 'USERNAME' in os.environ:  # local
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'local_database_username'
    app.config['MYSQL_PASSWORD'] = 'local_database_password'
    app.config['MYSQL_DB'] = 'local_database_name'
else:  # Heroku
    app.config['MYSQL_HOST'] = 'heroku_host'
    app.config['MYSQL_USER'] = 'heroku_database_username'
    app.config['MYSQL_PASSWORD'] = 'heroku_database_password'
    app.config['MYSQL_DB'] = 'heroku_database_name'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_details = request.form
        name = user_details['name']
        email = user_details['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()

        return redirect('/users')

    return render_template('index.html')


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM users")
    if result_value > 0:
        user_details = cur.fetchall()
        return render_template('users.html', userDetails=user_details)


if __name__ == '__main__':
    app.run()
