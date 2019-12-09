from flask import Flask, render_template

app = Flask(__name__) #creates an instance of Flask called app with variable __name__

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
