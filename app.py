import json, os, subprocess
from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from execution import exec_script
from utils import get_code
app = Flask(__name__)
CORS(app)

@app.route("/questions")
def Questions():
    with open('questions.json') as f:
        data = json.load(f)
        f.close()
    return json.dumps(data)

@app.route("/question", methods=['GET', 'POST'])
def Question():
    question_id = request.form['question_id']
    script = request.files['file']

    filename = secure_filename(script.filename)
    script.save(filename)

    response = {"results": exec_script(filename, question_id), "code": get_code(filename)}
    
    os.remove(filename)

    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True, port=5001)