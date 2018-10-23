import subprocess, json


def start(executable_file):
    return subprocess.Popen(
        ['python', executable_file],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def read(process):
    return process.stdout.readline().decode("utf-8").strip()
    
def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()

def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=2)

def exec_script(filename, question_id):
    response = []
    with open('answers/answers_{}.json'.format(question_id)) as f:
        data = json.load(f)
        f.close()
  
    for idx,inp in enumerate(data['inputs']): 
        process = start(f"./{filename}")
        write(process, inp)
        answer = read(process)
        terminate(process)
        write_answer = data['outputs'][idx]
        if answer == write_answer:
            if idx < 2:
                response.append({"input": inp, "answer": answer, "right_answer": write_answer, "correct": True})
            else:
                response.append({"input": inp, "answer": answer, "correct": True })
        else:
            response.append({"input": inp, "answer": answer, "correct": False})
    
    return response
