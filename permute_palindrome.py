
# Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴

# You can assume the input string only contains lowercase letters.

# Examples:

# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False
# "But 'ivicc' isn't a palindrome!"

# If you had this thought, read the question again carefully. We're asking if any permutation of the string is a palindrome. Spend some extra time ensuring you fully understand the question before starting. Jumping in with a flawed understanding of the problem doesn't look good in an interview.


def has_palindrome_permutation(the_string):
    
    if len(the_string) <= 1:
        return True
   
    track_values = {}
    
    for i in the_string:
        if i not in track_values:
            track_values[i] = 1
        else:
            track_values[i] += 1
            
    
    count_2 = 0
    count_1 = 0
    
    for key in track_values:
        if track_values[key] == 2:
            count_2 += 1
        elif track_values[key] == 1:
            count_1 += 1
    
    if count_1 > 1:
        return False
    else:
        return True

