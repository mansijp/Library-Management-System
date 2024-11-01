import os

from flask import Flask, render_template, request, url_for, redirect

base_dir = os.path.abspath(os.path.dirname(__file__))
folder = os.path.join(base_dir, '../webapp/templates')

app = Flask(__name__, template_folder=folder)

USERNAME = "john"
PASSWORD = "doe"

@app.route('/')
def home():
    return render_template('login.html', message='')

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['username']
    pword = request.form['password']

    if uname == USERNAME and pword == PASSWORD:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', message="Invalid credentials!")

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html',  message=f"Welcome back!")

@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
