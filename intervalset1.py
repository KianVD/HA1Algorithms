"""
Progammer: William Blanco
Navigator: Kian Drees
"""

def intervalset(intervals):

    allsubsets = [[]]
    for i in intervals:
        newsubtset = []
        for subset in allsubsets:
            newsubtset.append(subset + [i])
        #add all the new subsets to the list of all subsets
        allsubsets +=  newsubtset 
    # counter to keep track of the best solution
    best = 0

    for subset in allsubsets:
        subset.sort()
        valid = True
        for i in range(1,len(subset)): # compare each interval to the previous one
            current = subset[i][0]
            previousend = subset[i-1][1]
            if current < previousend:
                valid = False
                break   
        if valid and len(subset) > best: # if the subset is larger than the best, update best
            best = len(subset)
    return best

print(intervalset([(1,3),(2,5),(4,6),(6,8),(7,9)]))        

