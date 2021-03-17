# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Example 3:
# Input: root = []
# Output: 0

# Example 4:
# Input: root = [0]
# Output: 1
 
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        count = 0
        if root == None:
            return count
        
        def find_depth(current_node, count):
            if current_node == None:
                return count
            
            if current_node != None:
                count += 1
                
                return max(find_depth(current_node.right, count), find_depth(current_node.left, count))

                    
        
        left_count = (find_depth(root.left, count))
        right_count = (find_depth(root.right, count))

        return max(left_count + 1, right_count + 1)
        
# pseudocode
# define base case --> when node == Null
# call the function on the left side
# call the function on the right side
# join the results --> join with root count + 1