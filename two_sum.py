# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_pair = []
        
        for i in range(len(nums)):
            search_val = target - nums[i]
            if search_val in nums[i+1:]:
                index_pair.append(i)
                index_pair.append(nums.index(search_val, i+1)) # look up that this is the correct way to get val index
        
        return index_pair
                
        
# question: assuming that an answer *does* exist? or case when there's no answer & if so what to return?

# pseudocode:
    # track pointer to current index (or just loop through for i in range/len/nums)
    # check the value of current index relative to target & what's needed (i.e. 9 - 2 = 7)
    # check if that val (7) is in nums
        # if yes, get the index of that value
    # if not, move to the next index & do the same, repeat until we find the pair
    # return the pair