# turn two lists into sorted lists
# guaranteed sorted is a single list 
# using recursion

def make_lists_of_one(list):
    """Divide lists until reach a len of 1."""
    
    if len(lst) < 2:
        print(lst)
        return lst

    # index at half list
    mid = int(len(lst) / 2)

    # divide list in half
    make_lists_of_one(lst[:mid])
    # assign other half
    make_lists_of_one(lst[mid:])

def make_one_sorted_list(lst1, lst2):
    """Merge 2 sorted lists: ([1,3], [2,4]) => [1,2,3,4]"""

    result_list = []



lst2 = [2, 1, 7, 4, 5, 8]
make_lists_of_one(lst2)