from dataclasses import dataclass

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

def map_int(in_intervals, out_intervals, dst, src, size):
    new = []
    while in_intervals:
        interval = in_intervals.pop()
        result = map_interval(interval, dst, src, size)
        if result.moved:
            out_intervals.append(result.moved)
        new.extend(result.unmoved)
    return new

seeds_str, *maps = data.split("\n\n")
seeds = [int(x) for x in seeds_str.split()[1:]]

mappings = []
for m in maps:
    ranges = m.split("\n")[1:]
    mappings.append([tuple(int(a) for a in r.split()) for r in ranges])
    
def apply_mapping(intervals, mapping):
    out = []
    for interval in intervals:
        remaining = [interval]
        after = []
        for dst, src, size in mapping:
            remaining = map_int(remaining, after, dst, src, size)
        out.extend(remaining)
        out.extend(after)
    return out

from itertools import batched
intervals = [[s, s + 1] for s in seeds]
for mapping in mappings:
    intervals = apply_mapping(intervals, mapping)
assert min(i[0] for i in intervals) == 265018614

intervals = [[lo, lo + count] for lo, count in batched(seeds, 2)]
for mapping in mappings:
    intervals = apply_mapping(intervals, mapping)

assert min(i[0] for i in intervals) == 63179500