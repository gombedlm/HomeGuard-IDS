from flask import Flask, render_template, jsonify
from src.monitoring.monitoring import NetworkMonitor

app = Flask(__name__)
monitor = NetworkMonitor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/api/live-updates')
def live_updates():
    updates = monitor.get_live_updates()
    return jsonify(updates)

@app.route('/api/monitoring')
def monitoring():
    data = monitor.get_monitoring_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
