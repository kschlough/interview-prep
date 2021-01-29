# instructions

# The cake is not a lie!
# ======================

# Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble. 

# The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

# To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

# Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution("abcabcabcabc")
# Output:
#     4

# Input:
# solution.solution("abccbaabccba")
# Output:
#     2

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

# trying it recursively
# def solution(s, slice_count=0):
#     print(s)
#     print(slice_count)
#     # smallest = s
    
#     if len(s) % 2 == 0:
#         halfway = len(s) // 2
#         if s[:halfway] == s[halfway:]:
#             smallest = s[:halfway]
#             slice_count += 2
#             if len(smallest) % 2 != 0:
#                 return slice_count
#             else:
#                 solution(smallest, slice_count)
    
#     return slice_count
        
        # return smallest        
                    # just call it on one half of the list so the count is right?
                    # since they're dupes
                
    # return smallest

#     return slice_count


# trying with a loop
def solution(s):
    print(s)
    s = list(s)
    print(s)

    length = int(len(s))
    print(length)

    # steps counter unnecessary

    checklist = []

    for (i, m) in enumerate(s, start=0):
        print(m) 
        print(i)
        checklist.append(s[:i+1])

    print(checklist) 
    for item in checklist:
        item_length = len(item) 
        mult = length // item_length
        if (item * mult) == s:
            return mult


print(solution("abcabcabcabc"))
# # should return 4
print(solution("abccbaabccba"))
# # should return 2
print(solution("a"))
# # should return 1
print(solution("aaaaaaaaaaaaaaaaaa"))
# should return 18
print(solution("aabaabaabaabaabaabaab"))
# should return 7
print(solution("ooooooooooooooooof"))
# should return 1


# assumptions:
    # int return

# pseudocode   
# input: string, non-empty, letters a-z, less than 200 chars, clockwise
# output: int: max # of equal parts the string can be sliced into w/o leftovers 

# use mid points to split as many times as possible - because equal sequences will always be # equal too
# maybe do it recursively too? not sure if that'll end up faster or slower rt

# non-empty list so catch case:
    # if length is only one:
    # slice count equals one & return
    
# also: return max # equal parts, so if the len is uneven it's automatically 0
    # check if len of list is uneven meaning not modulo 2 I believe
    # if uneven, slice count equals zero & return
    ######## don't do this yet - can't use recursion if i do this, bc dividing list in half
    
# slice the list in half
# compare l1:l2
# if they're equal increase the slices count by 2
# if they're both longer than one:
    # call the function again on 11 & l2

# return slices count
    
    
