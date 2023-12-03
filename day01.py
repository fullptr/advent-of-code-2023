with open("day01_input.txt") as f:
    data = f.read()
    
mapping = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

total_part1 = 0
total_part2 = 0
for line in data.split("\n"):
    ints = [i for i in line if i.isdigit()]
    total_part1 += int(f"{ints[0]}{ints[-1]}")
    
    for key, val in mapping.items():
        line = line.replace(key, val)
        
    ints = [i for i in line if i.isdigit()]
    total_part2 += int(f"{ints[0]}{ints[-1]}")
    
print(total_part1, total_part2)