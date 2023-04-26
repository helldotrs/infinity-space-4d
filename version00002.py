import sys
import os
import json

class CoordinateSystem:
    def __init__(self, position=(0, 0, 0, 0), greetings=None):
        self.position = list(position)
        self.greetings = greetings or {
            (0, 0, 0, 0): "Welcome to the origin!",
            (2, 2, 2, 2): "Hello from the special coordinate!",
        }

    def move(self, direction, value):
        self.position[direction] += value

        coord = tuple(self.position)
        if coord in self.greetings:
            print(self.greetings[coord])

    def save(self, filepath):
        with open(filepath, "w") as file:
            json.dump({"position": self.position, "greetings": self.greetings}, file)

    def load(self, filepath):
        with open(filepath, "r") as file:
            data = json.load(file)

        self.position = data["position"]
        self.greetings = data["greetings"]

def main():
    coord_sys = CoordinateSystem()

    while True:
        command = input("Enter a command (move/save/load/exit): ")

        if command == "move":
            direction = int(input("Enter the direction (0/1/2/3): "))
            value = int(input("Enter the value to move: "))
            coord_sys.move(direction, value)
            print("Current position:", coord_sys.position)

        elif command == "save":
            filepath = input("Enter the file path to save: ")
            coord_sys.save(filepath)
            print("Saved position and greetings.")

        elif command == "load":
            filepath = input("Enter the file path to load: ")
            if os.path.exists(filepath):
                coord_sys.load(filepath)
                print("Loaded position and greetings.")
            else:
                print("File not found.")

        elif command == "exit":
            print("Exiting the program.")
            sys.exit()

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
