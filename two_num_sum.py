# algoexpert.io array problem

def twoNumberSum(array, targetSum):
    return_pair = []
	
	while array != []:
		check_val = array.pop()
		target_val = targetSum - check_val
		if target_val in array:
			return_pair.append(check_val)
			return_pair.append(target_val)
			break
	
	return return_pair



# using hash table (constant time lookup)
hash_table = {}

for num in array:
    val = target - num
    if val in hash_table:
        return [num, val]
    else:
        hash_table[val] = True

return []
