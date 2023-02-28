from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/dojo")
def dojo():
    return "dojo"

@app.route("/hi")
def hi():
    return "hi, jaime"


@app.route("/hi/<hi_id>")
def hipost(hi_id):
    return "hi, jaime" + str(hi_id)
