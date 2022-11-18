from flask import Flask,render_template, request

app = Flask(__name__)
app.secret_key="hiii"

@app.route("/")
def index():
	return render_template("Homepage.html")
	
@app.route("/login")                                      
def home():
	return render_template("Login.html")

@app.route("/registration")                                      
def form():
	return render_template("registration.html")