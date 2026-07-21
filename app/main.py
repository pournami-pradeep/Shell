import os
import sys



def echo(statement):
    return statement.strip()[4:].strip()


def type_command(statement):
    command = statement.strip()[4:].strip()
    if command in ["type", "echo", "exit"]:
        return f"{command} is a shell builtin"
    
    paths = os.environ.get("PATH").split(":")
    file_name = command
    for dir in paths:
        file_path = f"{dir}/{file_name}"
        if  os.path.exists(file_path):
            if os.access(file_path, os.X_OK):
                return f"{file_name} is {file_path}"
            return None
    return f"{file_name}: not found"
    
def main():

    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        statement = input()
        command = statement.split(" ")[0]
        if not command:
            continue
        if command == "exit":
            break
        elif command == "echo":
            print(echo(statement))
        elif command == "type":
            result = type_command(statement)
            if not result:
                continue
            print(result)
        else:
            print(f"{command}: command not found")
    
    


if __name__ == "__main__":
    main()
