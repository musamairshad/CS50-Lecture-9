from flask import Flask, render_template, request

app = Flask(__name__)  # This line means hey python turn this file into a
# Flask application.

@app.route("/")  # To tell the Flask when to call this index function.
def index():
    name = request.args.get("name")
    return render_template("index.html", name_of_person="Usama") # explicitly assign the name.
    # return render_template("index.html", name_of_person=name) # return the result of rendering a
# template called index.html. render means printed this file on the screen so to speak.

# decorator is a special type of function that modifies another function.