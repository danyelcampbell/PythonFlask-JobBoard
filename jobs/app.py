###Danyel Campbell
###December 9, 2019
###Job Board Web Application


from flask import Flask, render_template, g
import sqlite3

PATH = "db/jobs.sqlite3"

app = Flask(__name__) #creates an instance of Flask called app with variable __name__

def open_connection(): #connects to the specific database
    def getattr(g, '_connection', None):
        """returns the value of the _connection attribute of object g,
         if it's not found it will return None"""
        return _connection
    if _connection == None:
        _connection = g._connection = sqlite.connection(PATH)
    row_factory = sqlite3.Row
    return _connection

def execute_sql(sql, values, commit, single):
    connection = open_connection()
    values = ()
    commit = False
    single = False
    cursor = connection.execute(sql, values)
    return cursor
    if commit == True:
        results = connection.commit()
    else:
        if curs



#will tell Flask what URL to trigger the function
@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
