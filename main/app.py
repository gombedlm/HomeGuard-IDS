from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a secure secret key

# Simple list for demonstration; replace with secure authentication method
users = {
    'admin': 'password'
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

if __name__ == '__main__':
    app.run(debug=True)
