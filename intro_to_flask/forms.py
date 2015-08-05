<<<<<<< HEAD
from wtforms import TextField, TextAreaField, SubmitField
from flask_wtf import Form
 
=======
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import Required

>>>>>>> b5afde0820fdacffc665ee4a72db3e0fd3abf7f0
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")