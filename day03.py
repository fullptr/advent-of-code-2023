with open("day03_input.txt") as f:
    data = f.read().split("\n")
    
numbers = []
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
            numbers.append((curr_pos, curr))
            curr = None
            curr_pos = None
                
    if curr is not None:
        numbers.append((curr_pos, curr))
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

def print_point(x, y):
    if valid(x, y):
        print(data[y][x], end="")
    else:
        print("N", end="")

def print_all_numbers():
    for (x, y), number in numbers:
        for dx in range(x - 1, x + len(number) + 1):  # check above and below
            print_point(dx, y - 1)
        print()
        print_point(x-1, y)
        print(number, end="")
        print_point(x+len(number), y)
        print()
        for dx in range(x - 1, x + len(number) + 1):  # check above and below
            print_point(dx, y + 1)
        print(f"\n{number=}", touches_symbol(x, y, len(number)))
        print()

total = 0
for (x, y), number in numbers:
    if touches_symbol(x, y, len(number)):
        total += int(number)
        
print(total)