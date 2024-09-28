from flask import Flask

app = Flask(__name__)

@app.route('/')
def demo():
    return '<h1>Hello from Flask!</h1><img src="/static/mei.png" alt="flask">'