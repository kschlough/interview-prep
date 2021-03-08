# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2] 
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()


        while nums:
            compare = nums.pop()
            if len(nums) > 1:
                current = nums[len(nums)-1]
            else:
                return compare
            if compare == current:
                nums.pop()
            else:
                return compare


    
        
# assumption: there will never be more than 2 of a number?
        
# pseudocode
# sort the list - using sort(), takes less memory and same runtime O(n log n)
# using a stack (LIFO) - pop the last and compare to current 
# ex: [4,1,2,1,2] --> sorted [1, 1, 2, 2, 4]
# pop 4, compare to 2, they're not equal so return 4
# ex: [2,2,1] --> sorted [1, 2, 2]
# pop 2, compare to 2, they're equal so pop 2 and start again
# pop 1 and it's the last in the list so return 1

# - .sort() function will modify the list it is called on 
# - sorted() function will create a new list containing a sorted version of the list it is given  
# - sorted() function will not modify the list passed as a parameter