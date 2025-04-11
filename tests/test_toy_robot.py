import pytest
from models.table import Table
from models.toy_robot import ToyRobot
from services.command_service import CommandService

@pytest.fixture
def service():
    table = Table()
    robot = ToyRobot(table)
    return CommandService(robot)

def test_place_and_report(service):
    result = service.process("PLACE 0,0,North")
    assert result == "OK"
    assert service.process("REPORT") == "Current position: 0,0,NORTH"

def test_move_forward(service):
    service.process("PLACE 1,2,NORTH")
    service.process("MOVE")
    assert service.process("REPORT") == "Current position: 1,3,NORTH"

def test_turn_left(service):
    service.process("PLACE 0,0,NORTH")
    service.process("LEFT")
    assert service.process("REPORT") == "Current position: 0,0,WEST"

def test_turn_right(service):
    service.process("PLACE 0,0,NORTH")
    service.process("RIGHT")
    assert service.process("REPORT") == "Current position: 0,0,EAST"

def test_ignore_before_place(service):
    result = service.process("MOVE")
    assert result == ""
    assert service.process("REPORT") == ""

def test_ignore_out_of_table(service):
    service.process("PLACE 0,0,SOUTH")
    service.process("MOVE")
    service.process("LEFT")
    assert service.process("REPORT") == "Current position: 0,0,EAST"

def test_invalid_coordinates(service):
    assert service.process("PLACE -1,0,NORTH") == "Invalid coordinates"
    assert service.process("PLACE 5,5,NORTH") == "Invalid coordinates"

def test_invalid_direction(service):
    assert service.process("PLACE 1,1,NORTHEAST") == "Invalid direction"

def test_invalid_place_command_format(service):
    assert service.process("PLACE") == "Invalid PLACE command"
    assert service.process("PLACE 1,2") == "Invalid PLACE command"

def test_unknown_command(service):
    service.process("PLACE 0,0,NORTH")
    assert service.process("JUMP") == "Unknown command"