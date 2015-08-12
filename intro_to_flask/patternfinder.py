from datetime import datetime
import flask.ext.mysqldb 
#from main import mysql

class PatternFinder():
    patterns=[]
    database= None

    def __init__(self, db):
        self.database = db 
        current_time = datetime.now() #the current time or time the server starts running
        start_time = datatime.delta(minutes=2)
        
    #definition of a patterns    
    def addPattern(self,ftname,ftcolumn,val,stname):
        self.patterns.append({firsttablename:ftname,firsttablecolumn:ftcolumn,value:val,sectablename:stname})
        
    def retrievePattern():
        cur1 = mysql.connection.cursor()
        cur1.execute("SELECT * FROM profile")
        row = cur1.fetchone()
        #while row is not None:
        #    print(row)
        column_names = row.description
        column_names = [ i[0] for i in column_names ] # list of column names to be used in search
        
        # retrieving the values of the row selected 
        search_set = [cell for cell in row] 
        # list of values from the row in the table provided that will be searched for 
        curl2= mysql.connection.cursor()
        curl2.execute("SELECT * FROM PROFILE WHERE "+ column_names[0] +" !="+search_set[0]" AND "column_names[1]+"="+search_set[1]") 
        pass
    
