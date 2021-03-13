# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr_s = []
        
        for char in s.lower():
            if char.isalnum():
                arr_s.append(char)
        
        print(arr_s)
        original = "".join(arr_s)
        arr_s.reverse()
        print(arr_s)
        
        reverse_arr = "".join(arr_s)
        if original == reverse_arr:
            return True
        else:
            return False
        
        
# pseudocode
# use .strip to remove white spaces and special characters
# all .lower() too
# if s == s.reverse() then it's a palindrome