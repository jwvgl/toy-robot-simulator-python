# Toy Robot Simulator (Python)

A simple command-line simulator for a toy robot moving on a 5x5 grid.

## Problem Description

- The table is a 5x5 grid.
- There are no other obstructions on the table surface.
- All commands are ignored until a valid `PLACE` command is issued.
- The toy robot must not fall of the table during movement or at the initial placement.
- The toy robot ignores any command that would move it off the table.
- The toy robot can be placed, moved, and turned left and right.

## Commands

```text
PLACE X,Y,F      # Places toy robot on the table at position X,Y facing F (NORTH, EAST, SOUTH, WEST)
MOVE             # Moves toy robot one unit forward in the direction it is currently facing
LEFT             # Turn toy robot 90 degrees to the left
RIGHT            # Turn toy robot 90 degrees to the right
REPORT           # Outputs the current X,Y,F position of the toy robot
```
## Example Input

```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```
### Expected Output
```
Current position: 3,3,NORTH
```
## Running the App

```bash
# From project root directory
python main.py
```

Then follow the on-screen prompt to enter commands.

## Running Tests

```bash
pytest
```

## Project Structure
```
main.py                        # Console UI entry point
models/                        # App logic and models
services/                      # App logic
tests/                         # Pytest test suite
```