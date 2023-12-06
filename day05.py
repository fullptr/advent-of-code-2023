with open("day05_input.txt") as f:
    data = f.read()
    
def map_interval(
    interval, dst, src, size
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    lo, hi = interval
    
    if lo <= src and src + size < hi: # middle is mapped
        return [[dst, dst + size]], [[lo, src], [src + size, hi]]
    
    if src <= lo and hi < src + size: # whole interval is mapped
        return [[lo - src + dst, hi - src + dst]], []
    
    if src <+ lo < src + size:
        return [[lo - src + dst, dst + size]], [[src + size, hi]]
    
    if src <+ hi < src + size:
        return [[dst, hi - src + dst]], [[lo, src]]
    
    return [], [interval]

def map_int(in_intervals, out_intervals, dst, src, size):
    new = []
    while in_intervals:
        interval = in_intervals.pop()
        moved, unmoved = map_interval(interval, dst, src, size)
        out_intervals.extend(moved)
        new.extend(unmoved)
    in_intervals[::] = new
    
def map_value(val, mappers):
    for dst, src, size in mappers:
        if src <= val < src + size:
            return val - src + dst
    return val

def apply_all_mappings(val, mappings):
    for mapping in mappings:
        val = map_value(val, mapping)
    return val

seeds_str, *maps = data.split("\n\n")
seeds = [int(x) for x in seeds_str.split()[1:]]

mappings = []
for m in maps:
    ranges = m.split("\n")[1:]
    mappings.append([tuple(int(a) for a in r.split()) for r in ranges])
    
def apply_mapping(intervals, mapping):
    out = []
    for interval in intervals:
        before = [interval]
        after = []
        for dst, src, size in mapping:
            map_int(before, after, dst, src, size)
        out.extend(after)
        out.extend(before)
    return out

from itertools import batched
intervals = [[lo, lo + count] for lo, count in batched(seeds, 2)]
for mapping in mappings:
    intervals = apply_mapping(intervals, mapping)

print(min(i[0] for i in intervals))