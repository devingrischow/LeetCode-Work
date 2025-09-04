# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in [adjacent] plots.
#
# Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, 
# return `true` if `n` new flowers can be planted in the `flowerbed` 'without violating the no-adjacent-flowers rule' and `false` otherwise.
#
# *Example 1:
#   `Input:` flowerbed = [1,0,0,0,1], n = 1
#   `Output:` true
#
# * Example 2:
#   `Input:` flowerbed = [1,0,0,0,1], n = 2
#   `Output:` false
#
# *Constraints: 
# `1 <= flowerbed.length <= 2 * 104`
# `flowerbed[i]` is `0` or `1`.
# There are no two adjacent flowers in `flowerbed`.
# `0 <= n <= flowerbed.length`

from typing import List

class Solution:

    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowersThatCanBePlanted = 0

        # Iterate through the flower bed positions and preform the nesessary calculations for determening the 

        # Use a modified flowerbed array to determine if bed changes will interfere on its own changes
        modifiedFlowerbed = flowerbed

       
            


        for flowerPos in range(len(flowerbed)):
            print("Checking Flower#: ", flowerPos)
            isFlowerOrEmpty = modifiedFlowerbed[flowerPos]

            print("Is this position a flower or empty space: ", isFlowerOrEmpty)

            # If this space is a flower, nothing can happen
            # However if its a empty space, determine if the space around it can have flowers planted 

            if isFlowerOrEmpty == 0:
                # Empty Space
                # Check if the position behind and ahed of the flower is free, otherwise DONT PROCEED
                forwardPosition = flowerPos + 1
                backwardPosition = flowerPos - 1

                print("Forward Position: ", forwardPosition)
                print("Back Position: ", backwardPosition)
                
                # If backward position and forward position are free, then a flower can be planted 
                # With the determination the flower can be planted, modify the modified flowerbed with the updated plant 



                # 2 Main Crasher Edgecases
                #1. array of 1 
                #2. array of 2

                if len(flowerbed) == 1:
                    modifiedFlowerbed[flowerPos] = 1
                    flowersThatCanBePlanted += 1
                    
                # Check Start Position
                #Start position needs to just check 1 ahead, the back can be ignored
                elif flowerPos == 0:
                    #Similar to end and like the end pos check,
                    if flowerbed[1] == 0:
                        modifiedFlowerbed[flowerPos] = 1
                        flowersThatCanBePlanted += 1
                        
                # Check End Position
                #Checks the end position and the position behind it (taking the length of the array - 2)
                elif flowerPos == len(flowerbed) - 1:
                    #position IS end 

                    if flowerbed[len(flowerbed)-2] == 0:
                        #Back IS VALID

                        modifiedFlowerbed[flowerPos] = 1
                        flowersThatCanBePlanted += 1


                    #if its not successfull there, its not valid


                # Standard Position Check
                elif (modifiedFlowerbed[forwardPosition] == 0 and modifiedFlowerbed[backwardPosition] == 0):
                    modifiedFlowerbed[flowerPos] = 1
                    flowersThatCanBePlanted += 1

            else:
                print("Potted Plant")
                
        if flowersThatCanBePlanted >= n:
            return True
        else:
            return False
        






s = Solution()

c1 = s.canPlaceFlowers([1,0,0,0,1], 1)
print("Case 1 Result: ", c1, "\n")

c2 = s.canPlaceFlowers([1,0,0,0,1], 2)
print("Case 1 Result: ", c2, "\n")