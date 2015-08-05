#<<<<<<< HEAD
from flask.ext.wtf import Form , validators #, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from models import db, Officer
#from wtforms.validators import Required

"""
class SignupForm(Form):
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Create Profile")

 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True
"""
#=======
#<<<<<<< HEAD
#from wtforms import TextField, TextAreaField, SubmitField
#from flask_wtf import Form
 
#=======
#from flask.ext.wtf import Form

#from wtforms.validators import Required

#>>>>>>> b5afde0820fdacffc665ee4a72db3e0fd3abf7f0
#>>>>>>> 9a11b17c487508b577f33411dcf5017b8e19174c
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")