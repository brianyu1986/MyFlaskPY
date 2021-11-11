from flask import Flask, render_template


# 
app = Flask(__name__)

# 
@app.route("/")

# def index():
# 	return "<h1>Demo Page</h1>"
def index():
	return render_template("index.html")


@app.route("/user/<name>")

def user(name):
	return render_template("user.html", username = name)

