## plan
## 1. read the input file
## 2. get guard initial position
## 4. while the position is in range of the grid
## 5. if next position is a wall, change direction
## 5. Move the guard
## 6. count steps
from operator import add



def read_input(file_name):
    grid = []
    with open(file_name, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def get_guard_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                grid[i][j] = "."
                return [i, j]
    return [0, 0]

def turn(direction):
    if direction == "U":
        return "R"
    elif direction == "R":
        return "D"
    elif direction == "D":
        return "L"
    elif direction == "L":
        return "U"

def test_direction(grid, direction, position , direction_dict) -> bool:
    guard_test_direction = turn(direction)
    guard_test_position = position

    guard_test_init_pos = position
    guard_test_inti_dir = direction
    print(guard_test_init_pos, guard_test_inti_dir)
    print("--------------------")
    visited = set()

    while guard_test_position[0] > 0 and guard_test_position[0] < len(grid) - 1 and guard_test_position[1] > 0 and guard_test_position[1] < len(grid[0]) - 1:
        guard_next_test_position = list(map(add, guard_test_position, direction_dict[guard_test_direction]))
        if (str(guard_test_position), str(guard_test_direction)) in visited:
            return True
        #if str(guard_test_position) in visited_turn:
        #    return True
        if grid[guard_next_test_position[0]][guard_next_test_position[1]] == "#":
            guard_test_direction = turn(guard_test_direction)
        else:
            visited.add((str(guard_test_position), str(guard_test_direction)))
            guard_test_position = guard_next_test_position
    return False


def main():
    direction_dict = {
        "U": [-1, 0],
        "D": [1, 0],
        "L": [0, -1],
        "R": [0, 1]
    }


    guard_position = [0, 0]
    guard_direction = "U"
    guard_test_direction = ""

    grid = read_input("in")
    guard_position = get_guard_position(grid)
    walking = True
    visited = set()
    possible = 0

    while(walking):
        guard_next_position = list(map(add, guard_position, direction_dict[guard_direction]))
        visited.add(str(guard_position))
        if guard_next_position[0] < 0 or guard_next_position[0] >= len(grid) or guard_next_position[1] < 0 or guard_next_position[1] >= len(grid[0]):
            walking = False
            break

        if grid[guard_next_position[0]][guard_next_position[1]] == "#":
            grid[guard_position[0]][guard_position[1]] = "+"
            guard_direction = turn(guard_direction)

        else:
            grid[guard_next_position[0]][guard_next_position[1]] = "#"
            if test_direction(grid, guard_direction, guard_position, direction_dict):
                possible += 1
            grid[guard_next_position[0]][guard_next_position[1]] = "."
            guard_position = guard_next_position

            if str(guard_position) not in visited:
                grid[guard_position[0]][guard_position[1]] = "|" if guard_direction == "U" or guard_direction == "D" else "-"
            else:
                grid[guard_position[0]][guard_position[1]] = "+"

    for line in grid:
        print("".join(line))
    print(possible)



if __name__ == "__main__":
    main()
