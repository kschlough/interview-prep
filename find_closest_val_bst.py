def findClosestValueInBst(tree, target):
    	# recursive solution
	def helper_func(tree, target, closest):
		# base case: when current node is a leaf
		if tree == None:
			return closest

		if abs(target - closest) > abs(target - tree.value):
			closest = tree.value
		if target < tree.value:
			return helper_func(tree.left, target, closest)
		elif target > tree.value:
			return helper_func(tree.right, target, closest)
		else:
			return closest
			
	
	return helper_func(tree, target, tree.value)
	


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

		
		
# pseudocode
# track the most recent closest value as you step through the tree
# step through the tree by asking is the val closer to left or right, proceed based on that
# example: starting at 10, looking for 12:
# diff left is abs (12-5) = 7, diff right is abs (15-12) = 3, right is closer so move to right 
# set closest to right (15) and continue


# questions:
# will there be any negative #s? (decides whether to use abs() or not)
# dupes?