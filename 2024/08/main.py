from curses.ascii import isdigit
from curses.ascii import isalpha
import operator
lines = []
def read_input(file_name):
    lines = []
    with open(file_name, "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def get_antanas_postions(lines) -> list:
    x, y = 0, 0
    positions = []
    for x in range(0,len(lines)):
        for y in range(0, len(lines[x])):
            if lines[x][y].isdigit() or lines[x][y].isalpha():
                positions.append([[int(x), int(y)], lines[x][y]])
    return positions

def calculate_antinodes(positions, range_x, range_y) -> set:
    antinodes = set()
    for i in range(0, len(positions)):
        for j in range(0, len(positions)):
            if positions[i][1] == positions[j][1] and i != j:
                difference = list(map(operator.sub, positions[i][0], positions[j][0]))
                antinode_pos = list(map(operator.add, positions[i][0], difference))
                while antinode_pos[0] >= 0 and antinode_pos[0] <= range_x and antinode_pos[1] >= 0 and antinode_pos[1] <= range_y:
                    if str(antinode_pos) not in antinodes and antinode_pos not in positions:
                        print(antinode_pos)
                        antinodes.add(str(antinode_pos))
                    antinode_pos = list(map(operator.add, antinode_pos, difference))
    return antinodes

def main():
    lines = read_input("in")
    range_x = len(lines) - 1
    range_y = len(lines[0]) - 1
    positions = get_antanas_postions(lines)
    antinodes = calculate_antinodes(positions, range_x, range_y)
    for line in lines:
        print(line)
    tmp = 0
    for pos in positions:
        if str(pos[0]) in antinodes:
            tmp += 1
    print(len(antinodes) + len(positions) - tmp)


if __name__ == "__main__":
    main()
