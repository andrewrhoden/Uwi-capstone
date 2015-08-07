#<<<<<<< HEAD
from flask.ext.wtf import Form , validators #, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, FileField, validators
from models import db, Officer, Profile
#from wtforms.validators import Required
#
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
  name = TextField("Name", [validators.Required("Please enter your name.")])
  email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Subject", [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message", [validators.Required("Please enter a message.")])
  submit = SubmitField("Send")

class ProfileForm(Form):
    picture = FileField("Photo")
    gender = TextField("Gender")
    first_name = TextField("First Name")
    middle_name = TextField("Middle Name")
    last_name = TextField("Last Name")
    home_address = TextAreaField("Home Address")
    weapon_of_choice = TextField("Weapon Of Choice")
    height = TextField("Height")
    weight = TextField("Weight")
    build = TextField("Build")
    complexion = TextField("Complexion")
    hair_colour = TextField("Hair Colour")
    eye_colour = TextField("Eye Colour")
    ethnicity = TextField("Ethnicity")
    scars = TextField("Scars")
    work_address = TextAreaField("Work Address")
    work_contact_no = TextField("Work Contact Number")
    job_title = TextField("Job Title")
    mother_first_name = TextField("Mother's First Name")
    mother_maiden_name = TextField("Mother's Maiden Name")
    mother_surname = TextField("Mother's Surname")
    mother_address = TextAreaField("Mother's Address")
    mother_nationality = TextField("Mother's Nationality")
    father_first_name = TextField("Father's First Name")
    father_surname = TextField("Father's Surname")
    father_address = TextAreaField("Father's Address")
    father_nationality = TextField("Father's Nationality")
    submit = SubmitField("Update")