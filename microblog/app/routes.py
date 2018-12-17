#Aaina Vannan
#Ch.1 "A Hello, World" Flask Application
#defines logic of application
#displays "Hello World" when you put in URL and open that in web browser

#in order for the URL tag to work, it needs to import app package w/ the app variable in it
#from package import variable

from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
#URL tag above used to get to tag function
@app.route('/index')
def index():
    user = {"username" : "Aaina"}
    posts = [{"author": {"username":"Aaina"},
              "body" : "Hey how's life?" },
             { "author": { "username" : "Sarah"},
               "body" : "Why did you decide to take LINK? "}
            ]
    return render_template('index.html.py', title = 'Home',user = user, posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html.py', title = "Sign in", form = form)
#this template has everyhting!
#h1 = biggest type of font so it is used for getter
#we're mixing code with html here so we need to move html to a separate file
#the since it is index.html.py and not specific lines of code, it prints
#everything - including comments
#squigly brackets = posts
