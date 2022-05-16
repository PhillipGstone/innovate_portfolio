from flask import render_template, redirect, Blueprint, request, url_for
from favourites import empty, add_to_list

my_view = Blueprint('my_view', __name__) 

@my_view.route("/") 
def home():
    return render_template("home.html") 

@my_view.route("/contact")
def contact():
    return render_template("contact.html") 


@my_view.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        new_band = request.form["add_band"]
        add_to_list(new_band)
    return render_template("about.html", bands=empty) 

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.home")) 

