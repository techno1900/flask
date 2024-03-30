from flask import Flask

app = Flask(__name__)

@app.route('/<name>')

def inderx(name):
    return f'<h1> hello  {name}</h1>'



