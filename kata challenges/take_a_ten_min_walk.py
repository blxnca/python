from collections import Counter
def is_valid_walk(walk):
    counter = Counter(walk)
    keys = counter.keys()
    if (len(walk) != 10):
        return False
    if (counter.get('n') == counter.get('s')) and (counter.get('w') == counter.get('e')):
        return True
    else:
        return False

is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) #'should return True'
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) #'should return False'
is_valid_walk(['w']) #'should return False'
is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) #'should return False'