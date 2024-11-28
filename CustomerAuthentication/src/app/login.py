import os
from flask import Flask, render_template, request, url_for, redirect, session

base_dir = os.path.abspath(os.path.dirname(__file__))
templates_folder = os.path.join(base_dir, '../webapp/templates')
static_folder = os.path.join(base_dir, '../webapp/static')

app = Flask(__name__, template_folder=templates_folder, static_folder=static_folder)

app.secret_key = 'temporary_test_session_microservice1'

# hardcoded but to be integrated with mongoDB
USERNAME = "john"
PASSWORD = "doe"

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html', message='')

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['username']
    pword = request.form['password']

    if uname == USERNAME and pword == PASSWORD:
        # Store user information in the session
        session['username'] = uname
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', message="Invalid credentials!")


@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Check if the user is logged in by looking for the session variable
    if 'username' not in session:
        return redirect(url_for('home'))  # Redirect to login if not logged in

    return render_template('dashboard.html', message=f"Welcome back, {session['username']}!")


@app.route('/logout', methods=['POST'])
def logout():
    # Remove user session data
    session.pop('username', None)  # This clears the session
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
