
import os
import sys

import subprocess
HOME = os.environ.get('HOME')

def exit(statement):
    sys.exit()

def echo(statement):
    res = statement.strip()[4:].strip()
    if not "'" in res and not '"' in res:
        res = " ".join(res.split())

  
    print(res.replace("'","").replace('"',''))
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
    command = command.split("'")
    final_list = []
    for word in command:
        if word.strip():
            final_list.append(str(word).strip())

    # files = command.strip()[3:].strip()
    # file_list = files.split(".")
    # print(file_list)
    # final_list = []
    # for i in range(len(file_list)):
    #     file_name = file_list[i]+file_list[i+1]
    #     i += 2
    #     final_list.append(file_name)
    # print(final_list)
   
    # print(final_list)
    result = subprocess.run(final_list, check=True)
    if result.returncode == 0:
        print(result.stdout)

