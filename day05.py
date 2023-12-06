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

def map_intervals(intervals: list[Interval], dst: int, src: int, size: int):
    results = [map_interval(i, dst, src, size) for i in intervals]
    moved = [r.moved for r in results if r.moved]
    unmoved = []
    for result in results:
        unmoved.extend(result.unmoved)
    return unmoved, moved

def solve(intervals):
    for mapping in mappings:
        remaining = intervals
        intervals = []
        for dst, src, size in mapping:
            remaining, out = map_intervals(remaining, dst, src, size)
            intervals.extend(out)
        intervals.extend(remaining)
        
    return min(i[0] for i in intervals)

seeds_str, *maps = data.split("\n\n")
seeds = [int(x) for x in seeds_str.split()[1:]]

mappings = []
for m in maps:
    ranges = m.split("\n")[1:]
    mappings.append([tuple(int(a) for a in r.split()) for r in ranges])

part1 = [[s, s + 1] for s in seeds]
part2 = [[lo, lo + count] for lo, count in batched(seeds, 2)]
print(solve(part1), solve(part2))