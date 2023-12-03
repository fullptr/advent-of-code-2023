with open("day02_input.txt") as f:
    data = f.read()
    
    
def part1(cubes):
    limits = {"red": 12, "green": 13, "blue": 14}
    for cube in cubes:
        count, colour = cube.split(" ")
        if int(count) > limits[colour]:
            return False
    return True

def part2(cubes):
    mins = {"red": 0, "green": 0, "blue": 0}
    for cube in cubes:
        count, colour = cube.split(" ")
        mins[colour] = max(mins[colour], int(count))
    return mins["red"] * mins["green"] * mins["blue"]
    
total_part1 = 0
total_part2 = 0

for line in data.split("\n"):
    game_id, game = line.split(": ")
    
    game_id = int(game_id[5:])
    game = game.replace(";", ",").split(", ")  # ; is meaningless
    
    total_part1 += game_id if part1(game) else 0
    total_part2 += part2(game)
    
print(total_part1, total_part2)