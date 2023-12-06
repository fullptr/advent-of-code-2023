from dataclasses import dataclass
from itertools import batched

with open("day05_input.txt") as f:
    data = f.read()
    
Interval = tuple[int, int]
    
@dataclass
class MappingResult:
    moved: list[Interval]
    unmoved: list[Interval]
    
def map_interval(interval: Interval, dst: int, src: int, size: int) -> MappingResult:
    """
    Given an interval, map it according to the given parameters. Results contains an optional
    moved segment of the interval (if it overlapped) plus the remaining unmoved segments, if any.
    """
    lo, hi = interval
    
    if lo <= src and src + size < hi: # middle is mapped
        return MappingResult(moved=[(dst, dst + size)], unmoved=[(lo, src), (src + size, hi)])
    
    if src <= lo and hi < src + size: # whole interval is mapped
        return MappingResult(moved=[(lo - src + dst, hi - src + dst)], unmoved=[])
    
    if src <= lo < src + size:
        return MappingResult(moved=[(lo - src + dst, dst + size)], unmoved=[(src + size, hi)])
    
    if src <= hi < src + size:
        return MappingResult(moved=[(dst, hi - src + dst)], unmoved=[(lo, src)])
    
    return MappingResult(moved=[], unmoved=[interval])

def map_intervals(intervals: list[Interval], dst: int, src: int, size: int):
    """
    Apply the map_interval function to a list of intervals, and joins the results into one.
    """
    joined_result = MappingResult(moved=[], unmoved=[])
    for interval in intervals:
        result = map_interval(interval, dst, src, size)
        joined_result.moved.extend(result.moved)
        joined_result.unmoved.extend(result.unmoved)
    return joined_result

def solve(intervals):
    for mapping in mappings:
        remaining = intervals
        intervals = []
        for dst, src, size in mapping:
            result = map_intervals(remaining, dst, src, size)
            remaining = result.unmoved
            intervals.extend(result.moved)
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