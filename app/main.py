import sys

def echo(command):
    return command.strip()[4:].strip()
    
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
            print(echo(command))
        else:
            print(f"{command}: command not found")
    
    


if __name__ == "__main__":
    main()
