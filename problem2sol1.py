"""
Progammer: William
Navigator: Kian Drees

"""

def intervalset(intervals):

    allsubsets = [[]]
    for i in intervals:
        newsubtset = []
        for subset in allsubsets:
            newsubtset.append(subset + [i])
        allsubsets +=  newsubtset

    best = 0

    for subset in allsubsets:
        subset.sort()
        valid = True
        ):

