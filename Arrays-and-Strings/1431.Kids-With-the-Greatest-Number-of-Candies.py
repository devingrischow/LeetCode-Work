# There are `n` kids with candies. 
# You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `ith` kid has, 
# and an integer `extraCandies`, denoting the number of extra candies that you have.
#
# Return a 'boolean' array `result` of length `n`, where `result[i]` is `true` if, 
# after giving the `ith` kid all the `extraCandies`, they will have the [greatest] number of candies among all the kids, or false otherwise.
# 
# Note: that [multiple] kids can have the [greatest] number of candies.
#
# *Example 1: 
#   `Input:` candies = [2,3,5,1,3], extraCandies = 3
#   `Output:` [true,true,true,false,true]
# {Explanation:} If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
#
# *Example 2: 
#   `Input:` candies = [4,2,1,1,2], extraCandies = 1
#   `Output:` [true,false,false,false,false]
# {Explanation:} There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
#
# *Example 3:
#   `Input:` candies = [12,1,12], extraCandies = 10
#   `Output:` [true,false,true]
#
# *Constraints
# `n == candies.length`
# `2 <= n <= 100`
# `1 <= candies[i] <= 100`
# `1 <= extraCandies <= 50`

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        kidsWithToMuchCandy = []

        # Iterate through the candies, 

        for kidCandyAmount in candies:
            print("Kid Candy amount: ", kidCandyAmount)
            # For each kids candy amount, see what would happen if they recieved all the candy on top of their candy
            extraCandyGiven = kidCandyAmount + extraCandies
            
            print("Candy Amount after given to kid: ", extraCandyGiven)

            # With the extra candy calculated, go back and re check against each kid again 
            # To track if after each kid has more candies than his peers, use a counter to track every time they have more candy
            moreCandyThanOtherCount = 0

            for comparedCandy in candies:
                if extraCandyGiven >= comparedCandy:
                    #kis has more candy than kid, add 1
                    moreCandyThanOtherCount += 1
            
            print("Kid has more candy than this many of his peers: ", moreCandyThanOtherCount)

            # After seeing how much more candy the one kid has than others, see if they have more than everyone else 
            # If they do, then add true to the collection, 
            # If they dont, then add false.
            if moreCandyThanOtherCount == len(candies):
                kidsWithToMuchCandy.append(True)
            else:
                kidsWithToMuchCandy.append(False)


        return kidsWithToMuchCandy
        







s = Solution()

c1 = s.kidsWithCandies([2,3,5,1,3], 3)
print("Case 1 Result: ", c1, "\n")

c2 = s.kidsWithCandies([4,2,1,1,2], 1)
print("Case 2 Result: ", c2, "\n")

c3 = s.kidsWithCandies([12,1,12], 10)
print("Case 3 Result: ", c3, "\n")