

def get_code(filename):
    with open(f"./{filename}") as script:
        script_code = script.read()
    return ''.join(script_code)