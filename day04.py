with open("day04_input.txt") as f:
    data = f.read().split("\n")
    
part1 = 0
part2 = [1 for _ in data]
for idx, line in enumerate(data):
    winning, ours = line.split(": ")[1].split(" | ")
    count = len(set(winning.split()) & set(ours.split()))
    
    part1 += 2 ** (count - 1) if count != 0 else 0
    for offset in range(count):
        part2[idx + 1 + offset] += part2[idx]
    
print(part1, sum(part2))