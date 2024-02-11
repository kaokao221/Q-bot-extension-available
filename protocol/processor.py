import sys


def main():
    command = sys.argv[1]

    if command == "command1":
        print("Hello, world!")
    elif command == "command2":
        print("Goodbye, world!")


if __name__ == "__main__":
    main()
    input("Press Enter to exit")
