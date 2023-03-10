#dont bother importing all of flask, just import it as you need it
#python -m flask run :D
from flask import Flask, render_template, request, redirect, url_for
from forms import search_home_page
from flask_navigation import Navigation

#some basic info to give flask
app = Flask(__name__, template_folder='templates', static_folder='static')
nav = Navigation(app)

#nav bar stuff (not sure if this works for the footer as well)
nav.Bar('top',[
    nav.Item('Home', 'home'),
    nav.Item('About Us', 'about_us'),
    nav.Item('Technicals', 'technicals')
])

@app.route("/")
def home():
    return render_template('index.html')

#methods go in a list to let flask and jinja2 know what methods we'll be using on this certain page
@app.route("/search", methods=["GET", "POST"])
def home_search():
    #MAKE SURE TO RETURN THE FUNCTION THAT IS MADE IN FORMS!!!
    if request.method == "POST":
        return search_home_page()
    
    return search_home_page()

@app.route("/about_us")
def about_us():
    return render_template('aboutus.html')

@app.route("/technicals")
def technicals():
    return render_template('technicals.html')



