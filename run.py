import os   # standard python library
import json # standard json library because we have company.js file which will be used in about.html page
from flask import Flask, render_template #capital indicates that it is a class name, import as well render function so that I do not need to type html code


app = Flask(__name__)  #in Flask the variable is called app


@app.route("/") #Then, we use the route decorator to tell Flask what URL should trigger the function that follows.
def index():     #I will create a function called "index", which just returns the string, "Hello, World".
    return render_template("index.html")  # I need to have templates directory and inside the index.html file. "templates" directory should be at the same level as run.py file


@app.route("/about")
def about():
    data = [] # I initialize here the new empty list called data
    with open("data/company.json", "r") as json_data:  # I need to initialize python to open json file as read only and assign this file to a new variable json_data
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/carreers")
def carreers():
    return render_template("carreers.html", page_title="Carreers")

if __name__ == "__main__":  #if name is equal to "main" (both wrapped in double underscores), then we're going to run our app with the following arguments. The word 'main' wrapped in double-underscores (__main__) is the name of the default module in Python.
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),  #We're using the os module from the standard library to get the 'IP' environment variable if it exists, but set a default value if it's not found.
        port=int(os.environ.get("PORT", "5000")),  #It will be the same with 'PORT', but this time, we're casting it as an integer, and I will set that default to "5000", which is a common port used by Flask.
        debug=True)  #We also need to specify "debug=True", because that will allow us to debug our code much easier during the development stage. we should never have "debug=True" in a production application, or when we submit our projects for assessment.