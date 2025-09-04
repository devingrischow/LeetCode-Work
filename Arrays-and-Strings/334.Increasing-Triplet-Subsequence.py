# Given an integer array `nums`, return `true` if there 'exists a triple of indices' `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. 
# If no such indices exists, return `false`.
#
# *Example 1:
#   `Input:` nums = [1,2,3,4,5]
#   `Output:` true
# {Explanation}: Any triplet where i < j < k is valid.
#
# *Example 2:
#   `Input:` nums = [5,4,3,2,1]
#   `Output:` false
# {Explanation}: No triplet exists.
#
# *Example 3:
#   `Input:` nums = [2,1,5,0,4,6]
#   `Output:` true
# {Explanation}: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
#
# *Constraints:
# `1 <= nums.length <= 5 * 105`
# `-231 <= nums[i] <= 231 - 1`

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float('inf')
        second_min = float('inf')

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                print(first_min)
                print(second_min)
                print(num)
                return True

        print(num)
        print(first_min)
        print(second_min)
        return False 
    






s = Solution()

c1 = s.increasingTriplet([1,2,3,4,5])
print("Case 1 Result: ", c1, "\n")

c2 = s.increasingTriplet([5,4,3,2,1])
print("Case 2 Result: ", c2, "\n")

c3 = s.increasingTriplet([2,1,5,0,4,6])
print("Case 3 Result: ", c3, "\n")