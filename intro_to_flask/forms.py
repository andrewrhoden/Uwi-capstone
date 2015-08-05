<<<<<<< HEAD
from flask.ext.wtf import Form, Textfield, TextAreaField, SubmitField
=======
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import Required

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
>>>>>>> b5afde0820fdacffc665ee4a72db3e0fd3abf7f0
