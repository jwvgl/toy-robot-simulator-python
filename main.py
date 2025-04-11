from models.table import Table
from models.toy_robot import ToyRobot
from services.command_service import CommandService

def run_main_menu():
    table = Table()
    robot = ToyRobot(table)
    service = CommandService(robot)

    print("----------------Toy Robot Simulator----------------")
    print("Welcome to the Toy Robot Simulator!")
    print("Toy Robot Simulator simulates a toy robot moving on a 5x5 table.")
    print("---------------------------------------------------\n")

    while True:
        print("Choose an option:")
        print("1. Enter commands")
        print("2. Exit")
        option = input("Enter option: ").strip()

        if option == "1":
            run_input(service)
        elif option == "2":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1 or 2.\n")


def run_input(service):
    print("Enter commands line by line (enter 'BACK' to return):\n")
    while True:
        cmd = input("Enter command: ").strip().upper()
        if cmd == "BACK":
            break
        if not cmd:
            continue
        result = service.process(cmd)
        if result:
            print(result)

if __name__ == "__main__":
    run_main_menu()
