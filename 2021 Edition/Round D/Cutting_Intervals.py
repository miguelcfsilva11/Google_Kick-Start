import heapq

def cut(intervals, c):

    min_after = {}
    
    for interval in intervals:

        for i in range(interval[0] + 1, interval[1]):
            if i in min_after:
                min_after[i] += 1
            else:
                min_after[i] = 1
    heap = []

    for key in min_after:
        heap.append(-min_after[key])
    heapq.heapify(heap)

    counter = len(intervals)
    while len(heap) > 0 and c > 0:
        intervals = heapq.heappop(heap)
        counter -= intervals
        c -= 1
    return counter
            

t = int(input())
sample = 1
while t > 0:
    n, c = map(int, input().split())
    intervals = []
    while n > 0:
        interval = list(map(int, input().split()))
        intervals.append(interval)
        n -= 1
    t-=1
    sample += 1
    print(("Case #{0}: {1}").format(sample - 1, cut(intervals, c)))