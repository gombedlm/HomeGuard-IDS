# app.py

from flask import Flask, render_template
app = Flask(__name__)

# Route for the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
