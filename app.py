import json, os, subprocess
from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from execution import start, read, write, terminate
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
    script.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename))

    exec_script(filename, question_id)
    
    return json.dumps({ "ok": "ok"})

def exec_script(filename, question_id):
    
    with open('answers/answers_{}.json'.format(question_id)) as f:
        data = json.load(f)
        f.close()
  
    for idx,inp in enumerate(data['open']['inputs']): 
        process = start("./teste.py")
        write(process, ''.join(str(i) for i in inp))
        answer = read(process)
        terminate(process)
        print(answer)
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)

