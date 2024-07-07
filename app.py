# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Route for the dashboard
@app.route('/')
def dashboard():
    # Sample data (replace with actual data retrieval logic)
    recent_alerts = ["Alert 1", "Alert 2", "Alert 3"]
    connected_devices = 5
    internet_speed = "High"

    return render_template('dashboard.html', alerts=recent_alerts,
                           devices=connected_devices, speed=internet_speed)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
