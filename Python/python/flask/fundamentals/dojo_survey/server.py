from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = "123456"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data', methods=['POST'])
def datapass():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/survey')

@app.route('/survey')
def survey():
    return render_template('info.html')

if __name__=='__main__':
    app.run(debug=True)