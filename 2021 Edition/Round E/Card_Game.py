


import itertools

def factorial (n):
    
    res = 1
    
    for i in range(1, n + 1):
        res = res * i
    return res

t = int(input())
sample = 1
while t > 0:
    
    n = int(input())
    

    
    base_deck = []
    
    for j in range(1, n+1):
        base_deck.append(j)
        
    
    permutations = itertools.permutations(base_deck, len(base_deck))
    
    average = 0
    for deck in permutations:
        
        hand = [deck[0]]
        
        for card in deck:
            if card > hand[-1]:
                hand.append(card)
        
        average += len(hand)
    t -= 1
    sample += 1
    print(("Case #{0}: {1}").format(sample - 1, average / factorial(n)))