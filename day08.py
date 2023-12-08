from itertools import cycle
from math import lcm
    
with open("day08_input.txt") as f:
    directions, edges = f.read().split("\n\n")
    
graph = {}
for line in edges.split("\n"):
    src, dsts = line.split(" = ")
    graph[src] = dsts[1:-1].split(", ")

def get_cycle(start, is_sentinel):
    curr = start
    count = 0
    for d in cycle(directions):
        if is_sentinel(curr):
            return count
        
        if d == "L":
            curr = graph[curr][0]
        else:
            curr = graph[curr][1]
        count += 1
      
part1_sentinel = lambda n: n == "ZZZ"  
part1 = get_cycle("AAA", part1_sentinel)

part2_sentinel = lambda n: n.endswith("Z")
part2 = lcm(*[get_cycle(n, part2_sentinel) for n in graph if n.endswith("A")])

print(part1, part2)