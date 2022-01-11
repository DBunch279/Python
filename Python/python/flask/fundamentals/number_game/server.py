from flask import Flask, render_template, request, redirect, url_for
import random

rand_number = 0
hasGuessed = False
hasCompleted = False
color = ""
text = ""

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def start():
    global hasGuessed
    global hasCompleted
    global rand_number
    global color
    global text
    hasCompleted = False
    hasGuessed = False
    rand_number = random.randint(1, 100)
    if(request.method == "POST"):
        guess_number = request.form["input_number"]
        if(int(guess_number) == int(rand_number)):
            color = "Green"
            text = "You Guessed the Number it was " + str(rand_number)
            hasCompleted = True
        elif(int(guess_number) > int(rand_number)):
            color = "Red"
            text = "TOO BIG!"
        elif(int(guess_number) < int(rand_number)):
            color = "Red"
            text = "TOO SMALL!"
        hasGuessed = True
        return redirect(url_for("guess"))
    else:
        return render_template("index.html", methods=["POST", "GET"])

@app.route('/guess', methods=["POST", "GET"])
def guess():
    global hasGuessed
    global hasCompleted
    global rand_number
    global color
    global text
    if(request.method == "POST"):
        guess_number = request.form["input_number"]
        if(int(guess_number) == int(rand_number)):
            color = "Green"
            text = "You Guessed the Number it was " + str(rand_number)
            hasCompleted = True
        elif(int(guess_number) > int(rand_number)):
            color = "Red"
            text = "TOO BIG!"
        elif(int(guess_number) < int(rand_number)):
            color = "Red"
            text = "TOO SMALL!"
        
        return render_template("index.html", methods=["POST", "GET"], hasGuessed=hasGuessed, hasCompleted=hasCompleted, fillcolor=color, filltext=text)
    else:
        return render_template("index.html", methods=["POST", "GET"], hasGuessed=hasGuessed, hasCompleted=hasCompleted, fillcolor=color, filltext=text)

if __name__ == "__main__":
    app.run(debug=True)