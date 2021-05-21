from flask import Flask, escape, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my Watchlist"
    
@app.route('/user/<name>')
def user_name(name):
    return "username: %s"% escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('index'))
    print(url_for('user_name', name='greyli'))    
    print(url_for('index', num=1))
    print(url_for('test_url_for'))
    return 'Test page'
