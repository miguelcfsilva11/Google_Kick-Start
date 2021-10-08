
import itertools

t = int(input())
sample = 1

while t > 0:
    
    s = list(input())
    
    all_anagrams = list(itertools.permutations(s, len(s)))

    for j in all_anagrams:
        equal = True
        for i in range (len(s)):
            if s[i] == j[i]:
                equal = False

        if equal:
            t-=1
            sample +=1
            print(("Case #{0}: {1}").format(sample - 1,"".join(j)))
            break
    if not equal:
        t-=1
        sample +=1
        print(("Case #{0}: {1}").format(sample - 1,"IMPOSSIBLE"))