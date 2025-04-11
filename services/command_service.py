class CommandService:
    def __init__(self, robot):
        self.robot = robot

    def process(self, command: str) -> str:
        command = command.strip().upper()

        if command.startswith("PLACE"):
            try:
                coordinate = command[6:].split(",")
                x, y, facing = int(coordinate[0]), int(coordinate[1]), coordinate[2]
                return self.robot.place(x, y, facing)
            
            except Exception:
                return "Invalid PLACE command"
            
        if not self.robot.is_placed:
            return ""
        
        if command == "MOVE": return self.robot.move()
        elif command == "LEFT": return self.robot.left()
        elif command == "RIGHT": return self.robot.right()
        elif command == "REPORT": return self.robot.report()
        else: return "Unknown command"