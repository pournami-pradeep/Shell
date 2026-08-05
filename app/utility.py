
import os
import sys

import subprocess
HOME = os.environ.get('HOME')

def exit(statement):
    sys.exit()

def echo(statement):
    print(statement.strip()[4:].strip())
    return

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


def cd(statement):
    new_path = ""
    full_path = statement.strip()[2:].strip()
    if full_path.startswith("/"):
        if os.path.exists(full_path):
            os.chdir(full_path)
        else:
            print(f"cd: {full_path}: No such file or directory")
        return
   
    splitted_path = full_path.split("/")
    for path in splitted_path:
        if not path or path == ".":
            continue
      
        elif path == "..":
            cwd = os.getcwd()
            parent = os.path.dirname(cwd)
            new_path += parent 

        elif path == "~":
            new_path = HOME
        else:
            new_path += f"/{path}"
            
        if os.path.exists(new_path):
            os.chdir(new_path)
        else:
            print(f"cd: {full_path}: No such file or directory")
            break
    return 
  