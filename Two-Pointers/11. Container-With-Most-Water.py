#You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
# *Example 1:
# `Input:` height = [1,8,6,2,5,4,8,3,7]
# `Output:` 49
# `Explanation:` The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.
#
# *Example 2:
# `Input:` height = [1,1]
# `Output:` 1
#
# *Constraints:
# `n == height.length`
# `2 <= n <= 105`
# `0 <= height[i] <= 104`

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        heightLen = len(height)

        left = 0
        right = heightLen - 1

        maxArea = 0

        while left < right:
            # print(f'Left Pos: {left}')
            # print(f'Right Pos: {right}')

            leftWall = height[left]
            rightWall = height[right]

            # print(f"Left wall: {leftWall}, Right wall: {rightWall}")

            # Calculate the Area between the two `Positions`, and set the max area to the old max area and this one
            widthDiff = right - left

            newArea = widthDiff * min(leftWall, rightWall)
            # print(newArea)

            maxArea = max(maxArea, newArea)


            # Left Wall is shorter 
            if leftWall <= rightWall:
                left += 1
            # Right wall is shorter
            elif rightWall < leftWall:
                right -= 1
            


        return maxArea








s = Solution()


c1 = s.maxArea([1,8,6,2,5,4,8,3,7])
print(f'Case 1 Result: {c1}')