import os   # standard python library
from flask import Flask, render_template #capital indicates that it is a class name, import as well render function so that I do not need to type html code


app = Flask(__name__)  #in Flask the variable is called app


@app.route("/") #Then, we use the route decorator to tell Flask what URL should trigger the function that follows.
def index():     #I will create a function called "index", which just returns the string, "Hello, World".
    return render_template("index.html")  # I need to have templates directory and inside the index.html file. "templates" directory should be at the same level as run.py file


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/carreers")
def carreers():
    return render_template("carreers.html")

if __name__ == "__main__":  #if name is equal to "main" (both wrapped in double underscores), then we're going to run our app with the following arguments. The word 'main' wrapped in double-underscores (__main__) is the name of the default module in Python.
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),  #We're using the os module from the standard library to get the 'IP' environment variable if it exists, but set a default value if it's not found.
        port=int(os.environ.get("PORT", "5000")),  #It will be the same with 'PORT', but this time, we're casting it as an integer, and I will set that default to "5000", which is a common port used by Flask.
        debug=True)  #We also need to specify "debug=True", because that will allow us to debug our code much easier during the development stage. we should never have "debug=True" in a production application, or when we submit our projects for assessment.