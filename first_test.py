from flask import Flask
from markupsafe import escape

app = Flask(__name__) #Tells flask where to look for resources

@app.route("/") #Binds a function to a URL | Having <variable_name> passes it into the function 
def index():
    return f"<p>Index Page</p>"

@app.route("/user/<username>") #Binds a function to a URL | Having <variable_name> passes it into the function 
def show_user_profile(username):
    return f"User {escape(username)}!"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {subpath}"
# To run in debug mode (Updates while open):
# flask --app first_test run --debug