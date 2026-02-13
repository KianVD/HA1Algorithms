"""
Programmer: Kian Drees 
Navigator: William Blanco
"""


import math
#given nums, find contiguous subarray with largest sum
#brute force
def largestsubarray(nums):
    numslen = len(nums)
    largestsum = -math.inf
    for i in range(numslen):#one loop for each starting index
        for j in range(numslen):#one loop for each subset length
            subset = nums[i:i+j+1]#if index points out of range, python will just return what is already in the split
            subsetsum = sum(subset)
            if subsetsum > largestsum:
                largestsum = subsetsum

    return largestsum


print(largestsubarray([-2,1,-3,4,-1,2,1,-5,4]))

print(largestsubarray([1]))

print(largestsubarray([5,4,-1,7,8]))
