# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# pseudocode
# binary search tree - because you want the shortest / highest path - but it's not well-balanced?

# current node pointer initialized to root
# check which has children
# only do this for the leftmost or rightmost nodes not the inner
# keep count of # nodes, starting with count 1 for root
# if there's no children on a node, add 1 to count and then return the count 



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        current_level_nodes = [root]
        next_level_nodes = []
        current_depth = 1
        
        while True:
            while current_level_nodes:
                current_node = current_level_nodes.pop()
                
                if not current_node.left and not current_node.right:
                    return current_depth
                
                else:
                    if (current_node.left):
                        next_level_nodes.append(current_node.left)
                    if (current_node.right):
                        next_level_nodes.append(current_node.right)
                        
            current_depth += 1
            current_level_nodes, next_level_nodes = next_level_nodes, current_level_nodes
                
        return current_depth