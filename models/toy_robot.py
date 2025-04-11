Facing = ["NORTH", "EAST", "SOUTH", "WEST"]

class ToyRobot:
    LEFT_TURNS = {
        "NORTH": "WEST",
        "WEST": "SOUTH",
        "SOUTH": "EAST",
        "EAST": "NORTH"
    }
    RIGHT_TURNS = {
        "NORTH": "EAST",
        "EAST": "SOUTH",
        "SOUTH": "WEST",
        "WEST": "NORTH"
    }

    def __init__(self, table):
        self.table = table
        self.x = None
        self.y = None
        self.facing = None
        self.is_placed = False

    def place(self, x, y, facing):
        if facing not in Facing:
            return "Invalid direction"
        
        if not self.table.is_valid_position(x, y):
            return "Invalid coordinates"
        
        self.x, self.y, self.facing = x, y, facing
        self.is_placed = True
        return "OK"

    def move(self):
        if not self.is_placed: return ""

        moved_x, moved_y = self.x, self.y

        if self.facing == "NORTH": moved_y += 1
        elif self.facing == "EAST": moved_x += 1
        elif self.facing == "SOUTH": moved_y -= 1
        elif self.facing == "WEST": moved_x -= 1

        if self.table.is_valid_position(moved_x, moved_y):
            self.x, self.y = moved_x, moved_y
            return "OK"

    def left(self):
        if not self.is_placed: return ""

        self.facing = ToyRobot.LEFT_TURNS[self.facing]
        return "OK"

    def right(self):
        if not self.is_placed: return ""

        self.facing = ToyRobot.RIGHT_TURNS[self.facing]
        return "OK"

    def report(self):
        if not self.is_placed:
            return ""
        
        return f"Current position: {self.x},{self.y},{self.facing}"