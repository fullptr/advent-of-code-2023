from collections import Counter
from functools import cmp_to_key, partial

def parse_line(line):
    hand, score = line.split()
    return hand, int(score)
 
with open("day07_input.txt") as f:
    hands = [parse_line(line) for line in f]
    
def hand_type(hand: str):
    counts = Counter(hand)
    if len(counts) == 1:
        return 6
    if len(counts) == 2 and 4 in counts.values():
        return 5
    if len(counts) == 2:
        return 4
    if len(counts) == 3 and 3 in counts.values():
        return 3
    if len(counts) == 3:
        return 2
    if len(counts) == 4:
        return 1
    return 0

values_part1 = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

values_part2 = {k: v for k, v in values_part1.items()}
values_part2["J"] = 1

def remap_part1(hand):
    return hand

def remap_part2(hand: str):
    if "J" not in hand:
        return hand
    counts = Counter(hand)
    counts.pop("J")
    counts = counts.most_common()
    if not counts: # must have been JJJJJ
        return "AAAAA"
    return hand.replace("J", counts[0][0])

def compare_hands(lhs, rhs, remapper, values):
    lhs_hand, _ = lhs
    rhs_hand, _ = rhs
    
    lhs_type = hand_type(remapper(lhs_hand))
    rhs_type = hand_type(remapper(rhs_hand))
    if lhs_type < rhs_type:
        return -1
    if lhs_type > rhs_type:
        return 1
    
    for a, b in zip(lhs_hand, rhs_hand):
        if values[a] < values[b]:
            return -1
        if values[a] > values[b]:
            return 1
            
    return 0

part1_key = cmp_to_key(partial(compare_hands, remapper=remap_part1, values=values_part1))
part2_key = cmp_to_key(partial(compare_hands, remapper=remap_part2, values=values_part2))

hands = sorted(hands, key=part1_key)
part1 = sum(i * val for i, (_, val) in enumerate(hands, 1))
hands = sorted(hands, key=part2_key)
part2 = sum(i * val for i, (_, val) in enumerate(hands, 1))
print(part1, part2)