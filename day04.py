with open("day04_input.txt") as f:
    data = f.read().split("\n")
    
games = []
for line in data:
    winning, ours = line.split(": ")[1].split(" | ")
    into_set = lambda s: {int(x) for x in s.split()}
    games.append(len(into_set(winning) & into_set(ours)))
    
part1 = 0
part2 = [1 for _ in games]
for idx, count in enumerate(games):
    part1 += 2 ** (count - 1) if count != 0 else 0
    for offset in range(count):
        part2[idx + 1 + offset] += part2[idx]
    
print(part1, sum(part2))