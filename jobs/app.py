"""
Name: Danyel Campbell
Date: December 9, 2019
Title: Job Board Web Application
Purpose: TBD :D
"""


from flask import Flask, render_template, g
import sqlite3

PATH = "db/jobs.sqlite"

app = Flask(__name__) # creates an instance of Flask called app with variable __name__

def open_connection(): # connects to the specific database
    connection = getattr(g, '_connection', None) #returns the value of the _connection attribute of object g, if it's not found it will return None"""
    if connection == None:
        connection = g._connection = sqlite.connection(PATH)
    connection.row_factory = sqlite3.Row
    return connection

@app.teardown_appcontext
def close_connection(exception): # disconnects the database connection when app_context is torn down
    connection = getattr(g, '_connection', None)
    if connection is not None:
            connection.close()

def execute_sql(sql, values, commit, single):
    connection = open_connection()
    values = ()
    commit = False
    single = False
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    results = cursor.fetchone() if single else cursor.fetchall() # if a single result, fetch one, else fetch all
    return results


# will tell Flask what URL to trigger the function
@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
