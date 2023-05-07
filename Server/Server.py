import requests
from flask import Flask,request

app = Flask(__name__)

@app.route('/K9')
def k9():
    return "Wow"
@app.route('/addEmployee')
def addEmployee():
    print("Adding to DB...")
    print(request.get_json())
    return "Added employee " + request.get_json()

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