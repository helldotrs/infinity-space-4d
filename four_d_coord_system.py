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

        def move(values):
    global current_pos
    if len(values) != 4:
        print("Invalid number of arguments")
        print_usage()
    else:
        try:
            values = [int(v) for v in values]
            current_pos = [current_pos[i] + values[i] for i in range(4)]
            print(f"New position: {current_pos}")
            check_greetings()
        except ValueError:
            print("Invalid argument type")
            print_usage()
            
def show():
    print(f"Current position: {current_pos}")
    check_greetings()
def save(filename):
    with open(filename, "w") as f:
        data = {"current_pos": current_pos}
        json.dump(data, f)
    print(f"Saved to {filename}")

def load(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        global current_pos
        current_pos = data["current_pos"]
    print(f"Loaded from {filename}")
    show()
