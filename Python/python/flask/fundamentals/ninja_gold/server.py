from flask import Flask, request, render_template, redirect, session, url_for
import random
app = Flask(__name__)

color = "black"

app.secret_key="golden"
@app.route('/')
def index():
    session.clear()
    if "gold" not in session:
        session["gold"] = 0
    if "message" not in session:
        session["message"] = ""
    return render_template("index.html")

@app.route('/farm')
def farm_gold():
    gold_count = random.randint(10, 20)
    session["gold"] += gold_count
    color = "green"
    gold_message = f"<ul><li style='color: {str(color)};'>You have Gotten {str(gold_count)} Gold</li></ul>"
    return render_template("index.html", gold_message=gold_message)

@app.route('/cave')
def cave_gold():
    gold_count = random.randint(5, 10)
    color = "green"
    gold_message = f"<ul><li style='color: {str(color)};'>You have Gotten {str(gold_count)} Gold</li></ul>"
    session["gold"] += gold_count
    return render_template("index.html", gold_message=gold_message)

@app.route('/house')
def house_gold():
    gold_count = random.randint(2, 5)
    color = "green"
    gold_message = f"<ul><li style='color: {str(color)};'>You have Gotten {str(gold_count)} Gold</li></ul>"
    session["gold"] += gold_count
    return render_template("index.html", gold_message=gold_message)

@app.route('/casino')
def casino_gold():
    gold_count = random.randint(-50, 50)
    if(gold_count >= 0):
        color = "green"
        gold_message = f"<ul><li style='color: {str(color)};'>You have Gotten {str(gold_count)} Gold</li></ul>"
    else:
        color = "red"
        gold_message = f"<ul><li style='color: {str(color)};'>You have Gotten Burned. Lost {str(gold_count*-1)} Gold</li></ul>"
    session["gold"] += gold_count
    return render_template("index.html", gold_message=gold_message)
    
if __name__=='__main__':
    app.run(debug=True)