from flask import Flask, render_template, request

app = Flask(__name__) # This line means hey python turn this file into a 
# Flask application.

def index():
    return render_template("index.html") # return the result of index.html.

    