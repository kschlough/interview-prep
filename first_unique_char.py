# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
 

# Note: You may assume the string contains only lowercase English letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                
        for key in char_count:
            if char_count[key] == 1:
                return s.index(key)
        
        return -1