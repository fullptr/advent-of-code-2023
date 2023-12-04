with open("day04_input.txt") as f:
    data = f.read().split("\n")
    
games = []
for line in data:
    _, nums = line.split(": ")
    winning_str, ours_str = nums.split(" | ")
    winning = {int(x) for x in winning_str.split()}
    ours = {int(x) for x in ours_str.split()}
    games.append((winning, ours))
    
part1 = 0
part2 = [1 for _ in games]
for idx, (winning, ours) in enumerate(games):
    matches = ours & winning
    part1 += 2 ** (len(matches) - 1) if matches else 0
    for offset in range(len(matches)):
        part2[idx + 1 + offset] += part2[idx]
    
print(part1, sum(part2))