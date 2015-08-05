from flask import Flask, render_template
from forms import ContactForm

app = Flask(__name__) 
 
app.secret_key = '^534jskjfiuwrgskfmnb09872wvdbjm@76?*&'