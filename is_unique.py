# Cracking the Coding interview - ch. 1 arrays and strings

# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique(string):
    convert_array = list(string)

    while convert_array:
        check = convert_array.pop()
        if check in convert_array and check != " ":
            return False
    
    return True




# pseudocode
# if using data structures:
    # convert into an array --> o(n), but then pop from end and lookup in is O(1) for all remaining, so total O(n) runtime
    # pop off the end is least costly, so pop
    # compare if current letter is in array
    # if yes and not a " ", return no
    # if no, continue

# if not using add'l data structures:
    # sort the string so any dupes are next to each other -- can we use sort on a string bc it's immutable?
    # strip to remove white spaces as well
    # for char in string
        # if if next char is the same as current char, return yes
        # if not, keep going


# assumptions / questions
    # blank spaces should not count as duplicate characters
    # if other special characters shouldn't count? right now assumping !,: etc should count, otherwise could put in array to check against

# tests:
print(is_unique("abc")) # true
print(is_unique("abracadabra")) # false
print(is_unique("weinberg college faculty")) # false
print(is_unique("this far now")) # true - spaces should not count
