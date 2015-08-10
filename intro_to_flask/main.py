"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

#from intro_to_flask import app
from flask import Flask, render_template, session, request, redirect, url_for, flash, abort
from models import *
import jinja2
from forms import *
from flask.ext.mail import Message, Mail
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.jinja_loader = jinja2.FileSystemLoader('templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost/finalproject'

db.init_app(app)

app.secret_key = "tkssmartkodecodeWorldProdigy232323421@1127@6206birthd#2342)2**("


mail = Mail()
app.config["MAIL_SERVER"] = "smtp.live.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'uwimonaevals@outlook.com'
app.config["MAIL_PASSWORD"] = 'uwimonas;'

mail.init_app(app)

#mysql = MySQL(app)

@app.route('/testdb/')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
	return 'it works'
    else:
	return 'something is broke'


###
# Routing for your application.
###

@app.route('/')
def home(name=None):
    """Render the website's home page."""
    return render_template('home.html',name=name)
    

@app.route('/about/')
def about(name=None):
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/forms/')
def forms(name=None):
    """Render the website's forms page."""
    return render_template('forms.html')

@app.route('/profile/')
def profile(name=None):
    """Render the website's profile page."""
    return render_template('profile.html',name=name)
    
    
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    """Render the website's contact page."""
    #form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html',form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['uwimonaevals@gmail.com'])
            msg.body = """
            From: %s <%s> 
            To: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            
            return 'Form Submitted.'
    elif request.method == 'GET':
        return render_template('contact.html',form=form)


@app.route('/profile/edit/', methods=['GET', 'POST'])
def profileedit(name=None):
    """Render the website's edit profile page."""
    form = ProfileForm()
    if request.method == 'POST':
        profile = Profile(form.picture,form.home_address,form.gender,
        form.first_name ,form.middle_name,form.last_name,form.weapon_of_choice ,
        form.height,form.weight,form.build,form.complexion,form.hair_colour ,form.eye_colour ,
        form.ethnicity ,form.scars ,form.work_address ,form.work_contact_no,form.job_title ,form.mother_first_name 
        ,form.mother_maiden_name,form.mother_surname,form.mother_address,form.mother_nationality,
        form.father_first_name,form.father_surname ,form.father_address,form.father_nationality, datetime.now())
        db.session.add(profile)
        db.session.commit()
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('profileedit.html', form=form)
    


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('login.html', form=form)
    return render_template('login.html',form=form)
    
    
@app.route('/report/')
def report(name=None):
    """Render the website's about page."""
    return render_template('report.html',name=name)

@app.route('/report/edit/')
def reportadd(name=None):
    """Render the website's about page."""
    return render_template('reportedit.html',name=name)

@app.route('/login/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
   
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            new_officer = Officer(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
            db.session.add(new_officer)
            db.session.commit()
        return "[1] Create a new user [2] sign in the user [3] redirect to the user's profile"
    elif request.method == 'GET':
        return render_template('signup.html', form=form)
        
    
    """
        Search Feature To Query Specific Similarities Within The Database
    """    
@app.route('/search/', methods=['GET', 'POST'])
def search(name=None):
    form = UserSearch()
    if request.method == 'POST':
        return 'Searching...'
    """Render the website's UserSearch page."""
    return render_template('search.html',form=form)
    
    
    """
        Pattern Identified Feature To View Cases Or Reports With A High Degree Of Similarity
    """ 
@app.route('/patterns/')
def patterns(name=None):
    """Render the website's about page."""
    return render_template('patterns.html',name=name)
        
        
        
        
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

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9000)
