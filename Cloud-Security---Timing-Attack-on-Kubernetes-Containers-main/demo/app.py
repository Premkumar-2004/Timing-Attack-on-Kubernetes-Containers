import os
import time
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generates a random 24-byte secret key

# Simulated user database with hashed passwords
users = {
    'admin': generate_password_hash('SecurePass#2024'),
    'bob_user': generate_password_hash('User@Access#987')
}

@app.route('/', methods=['GET'])
def home():
    # Render the login page
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Retrieve username and password from form data
    username = request.form['username']
    password = request.form['password']
    user_hash = users.get(username)

    if user_hash and check_password_hash(user_hash, password):
        time.sleep(1)
        flash('Login successful!', 'success')
        return redirect(url_for('home'))  # Redirects to the home page after successful login
    else:
        flash('Login failed!', 'error')
        return redirect(url_for('home'))  # Redirects back to the home page even if login fails

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

