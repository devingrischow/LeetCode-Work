# You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, 
# starting with `word1`. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
# Return the merged string.
#
# *Example 1:
#   `Input:` word1 = "abc", word2 = "pqr"
#   `Output:` "apbqcr"
# {Explanation:} The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
# *Example 2:
#   `Input:` word1 = "ab", word2 = "pqrs"
#   `Output:` "apbqrs"
# {Explanation:} Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
#
# *Example 3:
#   `Input:` word1 = "abcd", word2 = "pq"
#   `Output:` "apbqcd"
# {Explanation}: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
#
# *Constraints:
# `1 <= word1.length, word2.length <= 100``
# `word1` and `word2` consist of lowercase English letters.


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ''

        #2 location holding variables to track the letter position of each word 
        word1Pos = 0
        word2Pos = 0


        totalLetters = len(word1) + len(word2)
        print("Total Letters: ", totalLetters)

        #The strings merge will happen while the mergedstrings 
        #length is not the same as the total letters available
        
        #Create the merged string by running until the merged string is as long as the total letters

        #During each loop 2 checks happen 
        #first checks if the word position is less than the length, 
        #if it is then the wordsposition is added to the merged string, and the position is increased 
        
        #This happens again for the second word 
        while len(mergedString) != totalLetters:
            if word1Pos < len(word1):
                mergedString += word1[word1Pos]
                word1Pos += 1

                print("Merged String after adding word 1 letter: ", mergedString)
            
            if word2Pos < len(word2):
                mergedString += word2[word2Pos]
                word2Pos += 1

                print("Merged String after adding word 2 letter: ", mergedString)

            
        print("Merged String: ", mergedString)
        
        return mergedString
    


solution = Solution()

case1 = solution.mergeAlternately('abc', 'pqr')
print("\n")
case2 = solution.mergeAlternately('ab', 'pqrs')
print("\n")
case3 = solution.mergeAlternately('abcd', 'pq')