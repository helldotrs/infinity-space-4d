import sys
import json

# Global variables
current_pos = [0, 0, 0, 0]
greetings = {
    (0, 0, 0, 0): "Welcome to the origin!",
    (2, 2, 2, 2): "Congratulations, you found the secret location!"
}

def main():
    # Check for command-line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "move":
            move(sys.argv[2:])
        elif command == "show":
            show()
        elif command == "save":
            save(sys.argv[2])
        elif command == "load":
            load(sys.argv[2])
        else:
            print("Invalid command")
            print_usage()
    else:
        print("No command specified")
        print_usage()
