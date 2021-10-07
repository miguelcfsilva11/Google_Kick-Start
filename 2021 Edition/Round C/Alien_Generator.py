def calculate(g):
    counter = 0
    for i in range(1, g + 1):
        
        k = i
        
        curr_sum = 0
        
        while curr_sum < g:
            
            curr_sum += k
            k = k + 1
        if curr_sum == g:
            counter += 1

        curr_sum = 0
    return counter


t = int(input())
sample = 1

while t > 0:
    
    g = int(input())
    
    sample += 1
    t -= 1

    print(("Case #{0}: {1}").format(sample - 1,calculate(g)))