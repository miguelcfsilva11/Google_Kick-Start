import heapq


t = int(input())
sample = 1

while t > 0:
    
    d, n, k = map(int, input().split(" "))
    
    day_happiness = {}
    
    for j in range (1, d + 1):
        day_happiness[j] = []
    
    while n > 0:
        h, s, e = map(int, input().split())
        for j in range(s, e +1):
            day_happiness[j].append(h)
        n -= 1
    

    max_day_score = 0
    for key in day_happiness:
        scores = [-x for x in day_happiness[key]]
        heapq.heapify(scores)

        i = k
        day_score = 0

        while len(scores) > 0 and k > 0:
            day_score -= heapq.heappop(scores)
            k -= 1
        k = i

        if day_score > max_day_score:
            max_day_score = day_score
    t -= 1
    sample += 1
    
    print(("Case #{0}: {1}").format(sample - 1, max_day_score))