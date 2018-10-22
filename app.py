import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/questions")
def Questions():
    with open('questions.json') as f:
        data = json.load(f)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)