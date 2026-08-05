
import os
import sys

import subprocess


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
    path = statement.strip()[2:].strip()
    splitted_path = path.split("/")
    for path in splitted_path:
        if path == ".":
            continue
        elif path == "..":
            cwd = os.getcwd()
            parent = os.path.dirname(cwd)
            os.chdir(parent)
        else:
            if os.path.exists(path):
                os.chdir(path)
            else:
                print(f"cd: {path}: No such file or directory")        
    return