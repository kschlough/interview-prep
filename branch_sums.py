class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	return calcSum(root, sum = 0)
	
	
def calcSum(root, sum, return_val = []):
	if root == None:
		return_val.append(sum)
		return return_val
	else:
		sum += root.value
		return calcSum(root.left, sum)
		return calcSum(root.right, sum)


# input: binary tree
# output: list of sums in branch order
# edge cases: empty tree? return 0 sum; single node: return that node
# function signature: given

# suboptimal: iteratively, break each child into its own sub-tree
# optimal: depth first search using recursion
	# since using recursion, base case: when you hit a leaf node with no right & no left
# tradeoffs (time, space) - recursion would be o(n) for the # branches
