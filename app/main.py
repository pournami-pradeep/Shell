import os
import sys

import subprocess

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
    command = statement.strip()[4:].strip()
    executable, _ = check_exec(command)
    if executable:
        result = subprocess.run(statement.split(" "),capture_output=True,text=True)
        return result
        
    return None


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
        

def main():
    functions = {"echo":echo, "type": type_command, "exec": check_exec, "pwd": pwd}
    while True:
        sys.stdout.write("$ ")
        statement = input()
        splitted_statment = statement.split(" ")
        command = splitted_statment[0]
        if command == "exit":
            break
        if not command:
            continue
        if command in functions:
            functions[command](statement)
            continue
        result = run_exec(statement)
        print(result)
        if result:
            print(result.stdout,end='')
            continue
        print(f"{command}: command not found")
    
    


if __name__ == "__main__":
    main()
