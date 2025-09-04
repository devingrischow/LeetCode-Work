# Given an integer array `nums`, 
# return (an array) `answer` such that `answer[i]` 
# is equal to the product of all the elements of `nums` except `nums[i]`.
#
# The product of any prefix or suffix of `nums` is [guaranteed] to fit in a 
# [32-bit] integer.
#
# You must write an algorithm that runs in `O(n)` time and without using the division operation.
#
# *Example 1:
#   `Input:` nums = [1,2,3,4]
#   `Output:` [24,12,8,6]
#
# *Example 2:
#   `Input:` nums = [-1,1,0,-3,3]
#   `Output:` [0,0,9,0,0]
#
# *Constraints:
# `2 <= nums.length <= 105`
# `-30 <= nums[i] <= 30`
# The input is generated such that `answer[i]` is [guaranteed] to fit in a 
# [32-bit] integer.

import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        #Fill res array with 1s
        result = [1] * numsLength
        print(result)

        prefix = 1

        for i in range(numsLength):
            # print("Result at point before math", i, ": ", result)
            # print("Prefix at Run before: ", prefix)

            result[i] = prefix
            
            print(f"{prefix}*={nums[1]}")
            prefix *= nums[i]
            

            # print("Result at point ", i, ": ", result)
            # print("Prefix at Run: ", prefix)

            
        # print("--Preform Suffix Calculations--")

        suffix = 1
        
        for i in range(numsLength - 1, -1, -1):
            # print("Result at point before math", i, ": ", result)
            # print("Suffix at Run before: ", suffix)

            
            
            print(f"{result[i]}*={nums[1]}")
            result[i] *= suffix

            suffix *= nums[i]
            

            # print("Result at point ", i, ": ", result)
            # print("Suffix at Run: ", prefix)
    
        return result
    






s = Solution()

c1 = s.productExceptSelf([1,2,3,4])
print("Case 1 Results: ", c1, "\n")

c2 = s.productExceptSelf([-1,1,0,-3,3])
print("Case 2 Results: ", c2, "\n")