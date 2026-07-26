import sys
from .utility import echo, type_command, pwd, run_exec, exit, cd
        
functions = {"echo":echo, "type": type_command, "pwd": pwd, "exit": exit, "cd": cd}
def main():
    
    while True:
        sys.stdout.write("$ ")
        statement = input()
        if not statement:
            continue
        splitted_statment = statement.split(" ")
        command = splitted_statment[0]
       
        if command in functions:
            functions[command](statement)
            continue
        
        run_exec(splitted_statment)
            

if __name__ == "__main__":
    main()
