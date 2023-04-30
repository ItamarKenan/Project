import requests
from flask import Flask

app = Flask(__name__)

@app.route('/K9')
def k9():
    return "Wow"

@app.route('/')
def origin():
    return "This is my server"

@app.route('/test')
def isHealthy():
    return "healthy"


if __name__ == "__main__":
    app.run(debug=True)
    response = requests.get("http://127.0.0.1:5000")
    print(response)