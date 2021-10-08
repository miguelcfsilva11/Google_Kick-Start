def arithmetic(grid):

    possible_missing = []
    
    if (grid[2][2] + grid[0][0]) % 2 == 0:
        possible_missing.append((grid[2][2] + grid[0][0])// 2)
    if (grid[0][1] + grid[2][1]) % 2 == 0:
        possible_missing.append((grid[0][1] + grid[2][1])// 2)
    if (grid[1][0] + grid[1][2]) % 2 == 0:
        possible_missing.append((grid[1][0] + grid[1][2])// 2)
    if (grid[0][2] + grid[2][0]) % 2 == 0:
        possible_missing.append((grid[0][2] + grid[2][0])// 2)
    
    
    counter = 0
    max_counter = 0
    
    for i in possible_missing:
        grid[1][1] = i
        
        if grid[0][0] + grid[0][2] == grid[0][1] * 2:
            counter += 1
        if grid[1][0] + grid[1][2] == grid[1][1] * 2:
            counter += 1
        if grid[2][0] + grid[2][2] == grid[2][1] * 2:
            counter += 1
            
        if grid[0][0] + grid[2][0] == grid[1][0] * 2:
            counter += 1
        if grid[0][1] + grid[2][1] == grid[1][1] * 2:
            counter += 1
        if grid[0][2] + grid[2][2] == grid[1][2] * 2:
            counter += 1    
        
        if grid[0][0] + grid[2][2] == grid[1][1] * 2:
            counter += 1
        if grid[2][0] + grid[0][2] == grid[1][1] * 2:
            counter += 1
        
        if counter > max_counter:
            max_counter = counter
        counter = 0
    return max_counter
    
t = int(input())
counter = 1

while t > 0:
    
    grid = []
    row = []
    
    col = 0
    while len(grid) < 3:

        row = list(map(int, input().split()))

        if len(row) == 2:
            last_el = row[-1]
            row.pop()
            row.append(1)
            row.append(last_el)
        
        grid.append(row)
    t -= 1
    counter += 1
    print('Case #{0}: '.format(counter - 1) + str(arithmetic(grid)))