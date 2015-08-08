from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()

class Officer(db.Model):
  __tablename__ = 'officer'
  userid = db.Column(db.INT, autoincrement=True, unique=True, primary_key = True)
  email_address = db.Column(db.VARCHAR(255), unique=True)
  password=db.Column(db.VARCHAR(255))
  role =db.Column(db.VARCHAR(255))
  division= db.Column(db.VARCHAR(255))
  station=db.Column(db.VARCHAR(255))
  name =db.Column(db.VARCHAR(255))
  
   
  def __init__(self, name, email, passcode):
    self.name = name.title()
    self.email = email.lower()
    self.set_password(passcode)
     
  def set_password(self, pword):
    self.passcode = generate_password_hash(pword)
   
  def check_password(self, pword):
    return check_password_hash(self.passcode, pword)
    
class Profile(db.Model):
    __tablename__= 'profile'
    profileid = db.Column(db.INT, nullable=False, unique=True, autoincrement=True , primary_key=True)
    picture = db.Column(db.BLOB)
    home_address = db.Column(db.VARCHAR(255))
    gender = db.Column(db.VARCHAR(255))
    first_name = db.Column(db.VARCHAR(255))
    middle_name = db.Column(db.VARCHAR(255))
    last_name  = db.Column(db.VARCHAR(255))
    weapon_of_choice = db.Column(db.VARCHAR(255))
    height = db.Column(db.NUMERIC(4,2))
    weight = db.Column(db.NUMERIC(6,2))
    build = db.Column(db.VARCHAR(255))
    complexion = db.Column(db.VARCHAR(255))
    hair_colour = db.Column(db.VARCHAR(255))
    eye_colour = db.Column(db.VARCHAR(255))
    ethnicity = db.Column(db.VARCHAR(255))
    scars = db.Column(db.VARCHAR(255))
    work_address = db.Column(db.VARCHAR(255))
    work_contact_no = db.Column(db.VARCHAR(255))
    job_title  = db.Column(db.VARCHAR(255)) 
    mother_first_name = db.Column(db.VARCHAR(255))
    mother_maiden_name = db.Column(db.VARCHAR(255))
    mother_surname = db.Column(db.VARCHAR(255))
    mother_address = db.Column(db.VARCHAR(255))
    mother_nationality = db.Column(db.VARCHAR(255))
    father_first_name = db.Column(db.VARCHAR(255))
    father_surname = db.Column(db.VARCHAR(255))
    father_address = db.Column(db.VARCHAR(255))
    father_nationality = db.Column(db.VARCHAR(255))
    date_created = db.Column(db.DATETIME)
    
    def __init__(self,picture,home_address,gender,first_name ,middle_name,last_name,weapon_of_choice ,height,weight,build,complexion
    ,hair_colour 
    ,eye_colour 
    ,ethnicity 
    ,scars 
    ,work_address 
    ,work_contact_no
    ,job_title 
    ,mother_first_name 
    ,mother_maiden_name
    ,mother_surname 
    ,mother_address
    ,mother_nationality 
    ,father_first_name
    ,father_surname 
    ,father_address
    ,father_nationality
    ,date_created):
        self.picture=picture.data 
        self.home_address=home_address.data
        self.gender =gender.data
        self.first_name =first_name.data
        self.middle_name=middle_name.data
        self.last_name  =last_name.data  
        self.weapon_of_choice =weapon_of_choice.data 
        self.height =height.data
        self.weight=weight.data
        self.build=build.data.lower()
        self.complexion=complexion.data.lower()
        self.hair_colour =hair_colour.data.lower() 
        self.eye_colour=eye_colour.data.lower()  
        self.ethnicity =ethnicity.data.lower() 
        self.scars =scars.data.lower() 
        self.work_address =work_address.data.lower() 
        self.work_contact_no=work_contact_no.data.lower()
        self.job_title =job_title.data.lower() 
        self.mother_first_name =mother_first_name.data.lower() 
        self.mother_maiden_name=mother_maiden_name.data.lower()
        self.mother_surname =mother_surname.data.lower() 
        self.mother_address=mother_address.data.lower()
        self.mother_nationality =mother_nationality.data.lower() 
        self.father_first_name=father_first_name.data.lower()
        self.father_surname=father_surname.data.lower()
        self.father_address=father_address.data.lower()
        self.father_nationality=father_nationality.data.lower()
        self.date_created=date_created
        
    def __repr__(self):
        return '<User %r>' % self.userid