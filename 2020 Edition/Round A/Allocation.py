#Allocation

t = int(input())
test_sample = 1
while t > 0:
    n, b = map(int, input().split(" "))
    houses = list(map(int, input().split(" ")))
    houses.sort()
    counter = 0
    for i in houses:
        if b >= i:
            counter += 1
            b -= i
    print(("Case #{0}: {1}").format(test_sample, counter))
    test_sample += 1
    t -= 1