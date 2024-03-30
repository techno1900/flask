from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/cool')
def cool():
    return "cools"


if __name__ == "__main__":
    app.run()

