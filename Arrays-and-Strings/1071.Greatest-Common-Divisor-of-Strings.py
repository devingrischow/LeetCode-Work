# For two strings `s` and `t`, we say "`t` divides `s`" 
# if and only if `s = t + t + t + ... + t + t`` (i.e., `t` is concatenated with itself one or more times).
#
# Given two strings `str1` and `str2`, return the largest string x such that x divides both str1 and str2.
#
# *Example 1:
#   `Input:` str1 = "ABCABC", str2 = "ABC"
#   `Output:` "ABC"
#
# *Example 2:
#   `Input:` str1 = "ABABAB", str2 = "ABAB"
#   `Output:` "AB"
#
# *Example 3:
#   `Input:` str1 = "LEET", str2 = "CODE"
#   `Output:` ""
#
# *Constraints:
# `1 <= str1.length, str2.length <= 1000`
# `str1` and `str2` consist of English uppercase letters.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        #Quickly get the smallest string to test against, 
        #easier to test against the smallest string
        shortestString = min(len1, len2)

        #Returns a validation condition for the string and gcd
        def validate(groupIteration:int) -> bool:
            print(f"Letter Iteration: {groupIteration}")

            print(f"Number Divisibility 1: {len1 % groupIteration}")
            print(f"Number Divisibility 1: {len2 % groupIteration}")

            # if len1 % groupIteration or 
            #using the sense that 1/0 is true/false with python

            # check if both st1 and st2 are made of multiples of base 
            if len1 % groupIteration or len2 % groupIteration:
                print("Group Incompatible")
                return False


            stringToBase1Ratio = len1 // groupIteration
            stringToBase2Ratio = len2 // groupIteration

            print("String to base ratio of string 1: ", stringToBase1Ratio)
            print("String to base ratio of string 2: ", stringToBase2Ratio)


            #finally return the checked value if BOTH the strings (str1+2) equal the new strings made up by each other, if they are 
            #that means you have the combination of letter ratios

            #base string to be st1
            #base changes by the group iteration (being the value being tested), the last letters being removed for each iteration
            base = str1[:groupIteration]

            print("Base Letters: ", base)

            addedBase1 = stringToBase1Ratio * base
            addedBase2 = stringToBase2Ratio * base 
            print("Combined Bases 1: ", addedBase1)
            print("Combined Bases 2: ", addedBase2)

            doesBase1EqualStr = str1 ==  addedBase1
            doesBase2EqualStr = str2 ==  addedBase2

            print("Does Combined Base 1 = ", doesBase1EqualStr)
            print("Does Combined Base 2 = ", doesBase2EqualStr)

            #Both MUST equal each other, as eventually they will equal out 
            return doesBase1EqualStr and doesBase2EqualStr






        #------------Bottom of Validate-------------------






        print("Checking Groupings")
        #loop through the shortest string, however start at the shortest string and step down by -1, 
        #doing this makes the testing string shorter to see if the word matches
        #allowing for the ability to check each combination of letters
        for letterIteration in range(shortestString, 0, -1):
            #validate the string, check if the letter itertations match together
            if validate(letterIteration):
                #str1 is used as the base string
                gcd = str1[:letterIteration]
                return gcd
        
        #when all of this fails or never reaches, then its guranteed the strings to be empty 
        return ""


s = Solution()

s.gcdOfStrings("ABCABC", "ABC")
print("\n")
s.gcdOfStrings("ABABAB", "ABAB")
print("\n")
s.gcdOfStrings("LEET", "CODE")
print("\n")

