import re

def get_code(filename):
    with open(f"./{filename}") as script:
        script_code = script.read()
    return ''.join(script_code)


def verify_script(filename):
    with open(filename) as f:
        data = ''.join(f.readlines())
        f.close()
    p = re.compile('import os|import shutil|import .*[,].*os| import.*[,].*shutil')

    if p.findall(data):
        return True
    else:
        return False