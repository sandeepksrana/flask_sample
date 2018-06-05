from flask import render_template
from .. import app

@app.route("/")
def main():
	#return 'Hello World!'
	return render_template("index.html")
