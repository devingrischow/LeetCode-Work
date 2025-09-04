# Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
#
# Note: that you must do this in-place without making a copy of the array.
#
# *Example 1:
#   `Input:` nums = [0,1,0,3,12]
#   `Output:` [1,3,12,0,0]
#
# *Example 2:
#   `Input:` nums = [0]
#   `Output:` [0]
#
# *Constraints:
# `1 <= nums.length <= 104`
# `-231 <= nums[i] <= 231 - 1`

from typing import List

class Solution:

    def __moveItemToBack(self, positionToSwitch:int ,nums: List[int]):
        print("Position to Switch ", positionToSwitch)

        itemToMove = nums.pop(positionToSwitch)

        nums.append(itemToMove)

        print("Changed Nums: ", nums)



    def moveZeroes(self, nums: List[int]) -> None:
        numsLength = len(nums)

        lastPosition = numsLength - 1

        print("NumsLength = ", numsLength)
        print("Last Position = ", lastPosition)

        p1 = 0
        p2 = lastPosition

        # Run while pointer 1 is less than the length of nums, and p2 is greater than 0
        while(p1 < numsLength and p2 > 0):
            p1Num = nums[p1]
            

            print("P1 Num: ", p1Num, "Position ", p1)

            if p1Num == 0:
                #Value is 0, MOVE THE ITEM TO THE END OF THE ARRAY
                self.__moveItemToBack(p1, nums)

                p1 = 0
            else:
                p1 += 1


            p2Num = nums[p2]
            print("P2 Num: ", p2Num, "Position ", p2)
            # If the position 2 is not zero, then move it inward 
            if p2Num == 0:
                self.__moveItemToBack(p2, nums)
            

            p2 -= 1

            
            


            print("New Nums: ", nums)







s = Solution()

tc1 = [0,1,0,3,12]
tc2 = [0]


s.moveZeroes(tc1)
print("Case 1 Results: ",tc1 , "\n")

s.moveZeroes(tc2)
print("Case 2 Results: ",tc2 , "\n")
