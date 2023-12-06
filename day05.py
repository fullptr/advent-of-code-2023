from dataclasses import dataclass
from itertools import batched

with open("day05_input.txt") as f:
    data = f.read()
    
Interval = tuple[int, int]
    
@dataclass
class MappingResult:
    moved: Interval | None
    unmoved: list[Interval]
    
def map_interval(interval: Interval, dst: int, src: int, size: int) -> MappingResult:
    """
    Given an interval, map it according to the given parameters. Results contains an optional
    moved segment of the interval (if it overlapped) plus the remaining unmoved segments, if any.
    """
    lo, hi = interval
    
    if lo <= src and src + size < hi: # middle is mapped
        return MappingResult(moved=(dst, dst + size), unmoved=[(lo, src), (src + size, hi)])
    
    if src <= lo and hi < src + size: # whole interval is mapped
        return MappingResult(moved=(lo - src + dst, hi - src + dst), unmoved=[])
    
    if src <+ lo < src + size:
        return MappingResult(moved=(lo - src + dst, dst + size), unmoved=[(src + size, hi)])
    
    if src <+ hi < src + size:
        return MappingResult(moved=(dst, hi - src + dst), unmoved=[(lo, src)])
    
    return MappingResult(moved=None, unmoved=[interval])

def map_int(intervals, dst, src, size):
    #return [map_interval(i, dst, src, size) for i in intervals]
    unmoved = []
    moved = []
    for interval in intervals:
        result = map_interval(interval, dst, src, size)
        if result.moved:
            moved.append(result.moved)
        unmoved.extend(result.unmoved)
    return unmoved, moved

def solve(intervals):
    for mapping in mappings:
        new_intervals = []
        for interval in intervals:
            remaining = [interval]
            for dst, src, size in mapping:
                remaining, out = map_int(remaining, dst, src, size)
                new_intervals.extend(out)
            new_intervals.extend(remaining)
        intervals = new_intervals
        
    return min(i[0] for i in intervals)

seeds_str, *maps = data.split("\n\n")
seeds = [int(x) for x in seeds_str.split()[1:]]

mappings = []
for m in maps:
    ranges = m.split("\n")[1:]
    mappings.append([tuple(int(a) for a in r.split()) for r in ranges])

part1 = [[s, s + 1] for s in seeds]
assert solve(part1) == 265018614

part2 = [[lo, lo + count] for lo, count in batched(seeds, 2)]
assert solve(part2) == 63179500

print(solve(part1), solve(part2))