# Given a string `s`, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# *Example 1:
#   `Input:` s = "IceCreAm"
#   `Output:` "AceCreIm"
# {Explanation:} 
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# *Example 2:
#   `Input:` s = "leetcode"
#   `Output:` "leotcede"
#
# *Constraints:
# `1 <= s.length <= 3 * 105`
# `s` consist of [printable ASCII] characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]

        # Use 2 pointers to point to different positions of the string

        

        vowelChars = []

        # An array is used to store the sentance, but with special identifiers to hold positions of vowels: <>
        modifiedCharsArray = []

        

        # Loop through the word and work with the opposite position 

        for letterPos in range(len(s)):
            print("Letter Pos: ", letterPos)

            letter = s[letterPos]
            
            # If the letter is a VOWEl, 
            if letter.lower() in vowels:
                # Take the vowel, add it to the vowelChars
                vowelChars.append(letter)
                # And append a special char sequence into the modified chars array, 
                modifiedCharsArray.append("<>")
                

            # If the letter is NOT a vowel
            else:
                # Add the letter to the modified chars array
                modifiedCharsArray.append(letter)

        print("Modified Chars: ", modifiedCharsArray)
        print("Array of Vowels: ", vowelChars)

        # Reverse the vowels 
        vowelChars.reverse()

        newString = ""

        # Now loop through the main string, and each time there is a special char retrieve it from the vowels array
        for charPos in range(len(modifiedCharsArray)):
            charToCheck = modifiedCharsArray[charPos]
            print("Checking char: ", charToCheck)

            #if the char is the special symbol, pop out a char from the vowels list, and append it 
            if charToCheck == "<>":
                vowelToAdd = vowelChars.pop(0)

                newString += vowelToAdd
            else:
                # Otherwise simply add the char to the string 
                newString += charToCheck
        

        return newString







s = Solution()

c1 = s.reverseVowels("IceCreAm")
print("Case 1 Result: ", c1, "\n")

c2 = s.reverseVowels("leetcode")
print("Case 2 Result: ", c2, "\n")