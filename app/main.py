import sys

def echo(command):
    return command.strip()[4:]
    
def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        elif command and command.split(" ")[0] == "echo":
            print(echo(command))
        else:
            print(f"{command}: command not found")
    
    


if __name__ == "__main__":
    main()
