# 3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! "

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5004)
