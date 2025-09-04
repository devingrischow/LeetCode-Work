# Given an input string `s`, reverse the order of the [words].
#
# A (word) is defined as a sequence of non-space characters. The [words] in `s` will be separated by at least one space.
#
# Return 'a string of the words in reverse order concatenated by a single space.'
#
# Note: that `s` may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. Do not include any extra spaces.
#
# *Example 1:
#   `Input:` s = "the sky is blue"
#   `Output:` "blue is sky the"
#
# *Example 2:
#   `Input:` s = "  hello world  "
#   `Output:` "world hello"
# {Explanation}: 
# Your reversed string should not contain leading or trailing spaces.
#
# *Example 3:
#   `Input:` s = "a good   example"
#   `Output:` "example good a"
# {Explanation}: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
# *Constraints:
# `1 <= s.length <= 104`
# `s` contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is [at least one word] in `s`.

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the sentance by spaces
        # Reverse split array
        # Loop through and re-combine, while removing all trailing portions 

        splitString = s.split()
        print("Splitted string: ", splitString)

        splitString.reverse()

        print("Reversed Split Array: ", splitString)

        reversedSentance = ""

        for wPos in range(len(splitString)):
            word = splitString[wPos]
            
            reversedSentance += word

            if wPos != len(splitString) - 1:
                reversedSentance += " "

        

        return reversedSentance







s = Solution()

c1 = s.reverseWords("the sky is blue")
print("Case 1 Result: ", c1, "\n")

c2 = s.reverseWords("  hello world  ")
print("Case 2 Result: ", c2, "\n")

c3 = s.reverseWords("a good   example")
print("Case 3 Result: ", c3, "\n")