"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

#from intro_to_flask import app
from flask import Flask, render_template, session, request, redirect, url_for, flash, abort, send_from_directory
from models import *
import jinja2
from forms import *
from flask.ext.mail import Message, Mail
from datetime import datetime
from flask.ext.mysqldb import MySQL
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = '/home/tkstman/Web/final/finalproj/intro_to_flask/static/img'
ALLOWED_EXTENSIONS = set(['png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'gif', 'GIF'])



app = Flask(__name__, template_folder='templates')
app.jinja_loader = jinja2.FileSystemLoader('templates')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'finalproject'


mysql = MySQL(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/photo/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
                               
                               
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
        file = request.files['picture']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
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
        term = request.form['searchField']
        drop_down = request.form['criterion']
        se_term = "'%"+term+"%'"
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM profile WHERE '''+drop_down+''' LIKE %s '''%(se_term))
        rv = cur.fetchall()
        res = rv[0]
        # test = res[1]
        reslst = []
        filename = res[1].split("<FileStorage: u'")[1].split("' ('image/png')>")[0]
        home_address, gender, first_name, middle_name, last_name, weapon_of_choice, height, weight, build, complexion, hair_colour, eye_colour = res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11], res[12], res[13]
        ethnicity, scars, work_address, work_contact_no, job_title, mother_first_name, mother_maiden_name, mother_surname, mother_address, mother_nationality = res[14], res[15], res[16], res[17], res[18], res[19], res[20], res[21], res[22], res[23]
        father_first_name, father_surname, father_address, father_nationality, date_created = res[24], res[25], res[26], res[27], res[28]
        
        # for i in range(1, len(res)):
            # reslst.append(i)
        return render_template('searchresult.html', rv=res, filename=filename, form=form, rv1=home_address, rv2=gender, rv3=first_name, rv4=middle_name, rv5=last_name, rv6=weapon_of_choice, rv7=height, rv8=weight, 
                                                        rv9=build, rv10=complexion, rv11=hair_colour, rv12=eye_colour, rv13=ethnicity, rv14=scars, rv15=work_address, rv16=work_contact_no, rv17=job_title, rv18=mother_first_name,
                                                        rv19=mother_maiden_name, rv20=mother_surname, rv21=mother_address, rv22=mother_nationality, rv23=father_first_name, rv24=father_surname, rv25=father_address,
                                                        rv26=father_nationality, rv27=date_created)
        # return str(rv)
        # return 'Searching...'
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
