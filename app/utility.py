
import os
import sys

import subprocess
HOME = os.environ.get('HOME')

def exit(statement):
    sys.exit()

def echo_v2(statement):
    statement = statement.removeprefix("echo ")
    state = ""
    res = ""
    i = 0
    while i < len(statement):
        letter = statement[i]
        if not state and letter == "\\":
            res += statement[i+1]
            i += 2
            continue
        elif letter in ["'", '"'] and not state:
            state = letter
        elif state and letter == state:
            state = ""
        elif letter == " " and not state:
            if res and res[-1] != " ":
                res += " "
        else:
            res += letter
        i += 1
    print(res)        
    

def check_exec(command):
    paths = os.environ.get("PATH").split(":")
    file_name = command
    for dir in paths:
        file_path = f"{dir}/{file_name}"
        if os.path.exists(file_path):
            if os.access(file_path, os.X_OK):
                return (True, file_path)
    return (False, None)

def run_exec(statement):
    command = statement[0]
    executable, _ = check_exec(command)
    if not executable:
        print(f"{command}: command not found")
        return
    
    result = subprocess.run(statement,capture_output=True,text=True)
    print(result.stdout,end='')


def type_command(statement):
    command = statement.strip()[4:].strip()
    if command in ["type", "echo", "exit", "pwd"]:
        print(f"{command} is a shell builtin")
        return

    executable, file_path = check_exec(command)
    if executable:
        print(f"{command} is {file_path}")
        return
    print(f"{command}: not found")
    return

def pwd(statement):
    print(os.getcwd())
    return

def go_to(path):
    if not path:
        return True
    if os.path.exists(path):
        os.chdir(path)
        return True
    return False

def cd(statement): 
    new_path = ""
    full_path = statement.strip()[2:].strip()
    if full_path.startswith("/"):
        res = go_to(full_path)
        if not res:
            print(f"cd: {full_path}: No such file or directory")
        return
   
    splitted_path = full_path.split("/")
    for path in splitted_path:
        if not path or path == ".":
            continue
      
        elif path == "..":
            cwd = os.getcwd()
            parent = os.path.dirname(cwd)
            go_to(parent)

        elif path == "~":
            go_to(HOME)   
        else:
            new_path += f"{path}/"            
  
    res = (go_to(new_path))
    if not res:
        print(f"cd: {full_path}: No such file or directory")
        
    return 
  


def cat_file(command):
    files_str = command.strip()[3:].strip()
    if files_str.startswith("'"):
        files = files_str.split("'")
    elif files_str.startswith('"'):
        files = files_str.split('"')
    else:
        files = files_str.split(" ")
    files.insert(0,'cat')
    final_list = []
    for word in files:
        if word.strip():
            final_list.append(str(word).strip())
    result = subprocess.run(final_list, check=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout, end='')
    return

