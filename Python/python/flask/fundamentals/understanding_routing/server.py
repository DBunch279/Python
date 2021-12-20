from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<string:name>")
def say(name):
    return f"Hi {name}"

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    arr = []
    for i in range(0, int(num)):
        arr.append(word)
    return f"{arr}"

if(__name__ == "__main__"):
    app.run(debug=True)