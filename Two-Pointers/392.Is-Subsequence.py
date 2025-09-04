# Given two strings `s` and `t`, return `true` if `s` is a "subsequence" of `t`, or `false` 'otherwise'.
#
# A "subsequence" of a string is a new string that is formed from the original string by deleting some 
# (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
# *Example 1:
#   `Input:` s = "abc", t = "ahbgdc"
#   `Output:` true
#
# *Example 2:
#   `Input:` s = "axc", t = "ahbgdc"
#   `Output:` false
# 
# *Constraints:
# `0 <= s.length <= 100`
# `0 <= t.length <= 104`
# `s` and `t` consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        #If either string is empty, its all invalid
        #Deal with it quickly
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False

        targetList = list(s)

        testingLettersList = list(t)

        print("Target List: ", targetList)

        # A running counter acting as the second pointer, pointing to which number is correct 
        checkingLetter = 0

        for letter in testingLettersList:

            letterToTestAgainst = targetList[checkingLetter]        

            print("Iteration Letter: ", letter)
            print("Letter to test against: ", letterToTestAgainst)
            # If the iterated letter is the same as the testing against letter, then increase the checking letter counter by 1, 
            # Meaning that one letter has been confirmed good, and check the next letter in the array
            if letter == letterToTestAgainst:
                checkingLetter += 1

        

            #Check if its a substring by checking if the checking letter value is greater than or equal to the length of testing letters array 
            targetListLen = len(targetList)
            isSubSequenceMatch = checkingLetter >= targetListLen

            print("Checking letter amount: ", checkingLetter)
            print("Len of target list ", targetListLen)
            print("Does Subsequence match: ", isSubSequenceMatch)
            if isSubSequenceMatch:
                return True

        return False
    





s = Solution()

c1 = s.isSubsequence("abc", "ahbgdc")
print("Case 1 Result: ", c1, "\n")

c2 = s.isSubsequence("axc", "ahbgdc")
print("Case 2 Result: ", c2, "\n")