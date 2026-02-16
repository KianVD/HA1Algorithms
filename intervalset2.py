"""
Programmer: William Blanco
Navigator: Kian Drees
this is the optimized version of the interval set problem
"""

def intervalset(intervals):

    intervals.sort()

    best = 0
    lastend = -1

    for i in intervals:
        start = i[0]
        end = i[1] # keeps track of the end of the last interval in the set

        # if the start of the current interval is greater than or equal to the end of the last interval we can add it to the set
        if start >= lastend:
            best += 1
            lastend = end

        elif end < lastend:
            lastend = end

    return best         

print(intervalset([(1,3),(2,5),(4,6),(6,8),(7,9)]))