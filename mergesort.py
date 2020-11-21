# turn two lists into sorted lists
# guaranteed sorted is a single list 
# using recursion

def make_lists_of_one(lst):
    """Divide lists until reach a len of 1."""
    
    # if len lst is 1, return the lst
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

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            result_list.append(lst1.pop(0))
        else:
            result_list.append(lst2.pop(0))

    return result_list

# lst1 = [1, 4, 8]
# lst2 = [2, 7, 5]
# make_one_sorted_list(lst1, lst2)


lst2 = [2, 1, 7, 4, 5, 8]
# make_lists_of_one(lst2)


def merge_sort(lst):

    if len(lst) < 2:
        return lst

    mid = int(len(lst) / 2) 

    left_half_sorted = merge_sort(lst[:mid])
    right_half_sorted = merge_sort(lst[mid:])  

    return make_one_sorted_list(left_half_sorted, right_half_sorted)  

lst2 = [2, 1, 7, 4, 5, 8]
print(merge_sort(lst2))