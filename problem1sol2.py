"""
Programmer: Kian Drees 
Navigator: William Blanco
"""

import math
#given nums, find contiguous subarray with largest sum
#efficient
def largestsubarray(nums):
    numslen = len(nums)
    res = nums[0]
    maxEnding = nums[0] #initialize to first number
    #calculate the maximum sum ending at current element, for each element (induction)
    for i in range(numslen-1):#skip first element
        #find the maximum between the maxEnding at previous element plus current element and current element by itself (local maximum)
        maxEnding = max(maxEnding + nums[i+1], nums[i+1])
        #compare this maxEnding to the current global maximum res
        res = max(res,maxEnding)

    return res


print(largestsubarray([-2,1,-3,4,-1,2,1,-5,4]))

print(largestsubarray([1]))

print(largestsubarray([5,4,-1,7,8]))
