from flask import Flask, render_template, jsonify, request
from src.monitoring.monitoring import NetworkMonitor
from src.logging.logging import Logger
from src.alerting.alerting import Alerting

app = Flask(__name__)

# Initialize components
monitor = NetworkMonitor()
logger = Logger()
alerter = Alerting()

# Routes
@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/monitoring')
def monitoring():
    try:
        all_interfaces = monitor.get_all_interfaces()
        connected_wifi = monitor.get_connected_wifi()
        anomalies = []  # Placeholder for anomalies until method added
        # anomalies = monitor.detect_anomalies(all_interfaces + connected_wifi)
        return render_template('monitoring.html', all_interfaces=all_interfaces, connected_wifi=connected_wifi, anomalies=anomalies)
    except Exception as e:
        logger.error(f"Exception in monitoring route: {str(e)}")
        return render_template('error.html', error_message=str(e))

@app.route('/about')
def about():
    return render_template('about.html')

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
