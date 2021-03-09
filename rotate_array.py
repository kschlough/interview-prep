# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105


# queue: LIFO, pop() from the end append to the front

# pseudocode - 1st way
    # pop off the last bit of the array eg nums[k:end]
    # append it to the front

# pseudocode - 2nd way
    # pop off the first bit of the array eg nums[:k]
    # append to the end

# pseudocode - 3rd way

# option #1 o(n) insertion
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
            
        while i < k:
            val = nums.pop()
            nums.insert(0, val)
            i += 1
            
        return nums
        

        
        
        
