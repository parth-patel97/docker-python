from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
    
@app.route("/home")
def home():
    return 'Welcome to home page!'

@app.route("/about")
def about():
    return 'About Us'
