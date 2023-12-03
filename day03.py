with open("day03_input.txt") as f:
    data = f.read().split("\n")
    
numbers = {}
symbols = {}
    
for y, row in enumerate(data):
    curr = None
    curr_pos = None
    for x, value in enumerate(row):
        if value.isdigit():
            if curr is None:
                curr = value
                curr_pos = (x, y)
            else:
                curr += value
            continue
        if value != ".":
            symbols[x, y] = value
        if curr is not None:
            numbers[curr_pos] = curr
            curr = None
            curr_pos = None
                
    if curr is not None:
        numbers[curr_pos] = curr
    curr = None
    curr_pos = None
        
def valid(x, y):
    return 0 <= y < len(data) and 0 <= x < len(data[0])
        
def touches_symbol(x, y, length):
    """
    Returns true if the number starting at (x, y) of the given length touches a symbol.
    """
    for dx in range(x - 1, x + length + 1):  # check above and below
        for dy in (y - 1, y + 1):
            if (dx, dy) in symbols:
                return True
            
    return (x - 1, y) in symbols or (x + length, y) in symbols  # check the ends
        
def get_num_at(x, y):
    """
    Given a position in the grid, return the number that it is part of as well as the starting
    position, otherwise None
    """
    if not (valid(x, y) and data[y][x].isdigit()):
        return None, None
    while valid(x - 1, y) and data[y][x-1].isdigit():
        x -=1  # go to front of number
    return (x, y), numbers[x, y]
        
def get_surrounding_numbers(x, y) -> list[int]:
    """
    Returns all numbers adjacent to the given point
    """
    nums = {}
    for dy in (y-1, y, y+1):
        for dx in (x-1, x, x+1):
            if dx == x and dy == y: continue
            num_pos, num = get_num_at(dx, dy)
            if num is not None:
                nums[num_pos] = num
      
    return list(nums.values())

total1 = 0
for (x, y), number in numbers.items():
    if touches_symbol(x, y, len(number)):
        total1 += int(number)
        
print(total1)

total2 = 0
for (x, y), symbol in symbols.items():
    if symbol == "*":
        s = get_surrounding_numbers(x, y)
        if len(s) == 2:
            total2 += int(s[0]) * int(s[1])
print(total2)