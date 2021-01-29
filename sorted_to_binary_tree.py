# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums:
            return None
        
        root_index = len(nums) // 2
        root = nums[root_index]
        
        # instantiate tree
        return_tree = TreeNode(val = root)

        if len(nums) >= 2:
            return_tree.left = self.sortedArrayToBST(nums[:root_index])
            return_tree.right = self.sortedArrayToBST(nums[root_index+1:])
        
        # return the treenode
        return return_tree
        

# pseudocode
# set middle of sorted array to root
# divide length by two 
    # nodes to left are less than root value, nodes to right are greater
# repeat same process
# base case - at a leaf, no more nodes


# example

# [-10,-3,0,5,9]
# len 5 / 2 = 2
# root = 0
    # append root to return list // [0, -3]
        # TreeNode(val = 0)
# [-10,-3, 0, 5, 9]
    # create the tree node w/ given list
        # TreeNode(root, left=(nums[:root]), right=[root+1:])
    # call recursively to keep calling left & right
            # TreeNode.left = recurse_function(left)
            # TreeNode.right = recurse_function(right)
    # next call:
        # left [-10, -3]
        # right [5, 9]
    
    
    # variables to track left list index and right list index (when we reach 0, end of the node, return the tree list)
    # call function recursively on the lists

# repeat same process on left
# end condition met - [-10] [-3]
# and on right
# [5] [9]
