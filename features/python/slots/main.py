from utils.commands import commands
import sys


def main():
    """
    Executes functions based on a command-line argument.

    This function checks if a command-line argument is provided and matches a key in the 'commands' dictionary. 
    If matched, it executes the corresponding function. Otherwise, it outputs an error message or prompts 
    for a valid command.

    Usage:
    - python main.py [command]
    """
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command in commands:
            # Execute the function corresponding to the command
            commands[command]()
        else:
            print(f"Comando desconocido: {command}")

    else:
        print("Por favor, proporciona un comando.")


if __name__ == "__main__":
    main()