"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from intro_to_flask import app
from flask import Flask
from flask import render_template, request, redirect, url_for
from models import db
#from flask.ext.mysqldb import MySQL
#app = Flask(__name__)


#mysql = MySQL(app)

@app.route('/testdb/')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken'
    
    
    
    
    
    
    """= mysql.connection.cursor()
    cur.execute('''SELECT userid FROM mysql.officer''')
    rv = cur.fetchall()
    return str(rv)
"""
#if __name__ == '__main__':
#    app.run(debug=True)
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    

@app.route('/about/')
def about(name=None):
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile/')
def profile(name=None):
    """Render the website's about page."""
    return render_template('profile.html',name=name)

@app.route('/profile/edit/')
def profileedit(name=None):
    """Render the website's about page."""
    return render_template('profileedit.html',name=name)

@app.route('/login/')
def login(name=None):
    """Render the website's about page."""
    return render_template('login.html',name=name)

  
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


