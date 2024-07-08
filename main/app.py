# app.py

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Index route
@app.route('/')
def index():
    return render_template('dashboard.html')

# Settings route
@app.route('/settings')
def settings():
    return render_template('settings.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Monitoring route
@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

