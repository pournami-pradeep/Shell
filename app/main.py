import sys

def echo(statement):
    return statement.strip()[4:].strip()

def type_command(statement):
    command = statement.strip()[4:].strip()
    if command in ["type", "echo", "exit"]:
        return f"{command} is a shell builtin"
    return f"{command}: not found"
    
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
            print(type_command(statement))
        else:
            print(f"{command}: command not found")
    
    


if __name__ == "__main__":
    main()
